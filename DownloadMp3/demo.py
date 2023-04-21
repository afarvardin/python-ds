import os
from bs4 import BeautifulSoup
import requests
website_content = requests.get(web_root.strip()).text

soup = BeautifulSoup(website_content, features='html.parser')

author_list = []
# We search for the author keywords list:
for line in soup.find_all('td', class_='lista-libros1'):
    for element in line.find_all('a'):
        author_key = element.get('href')
        if not author_key:
            continue
        else:
            author_list.append(author_key)


def get_author_keywords(web_root):
    website_content = requests.get(web_root.strip()).text
    soup = BeautifulSoup(website_content, features='html.parser')

    author_list = []
    # We search for the author keywords list:
    for line in soup.find_all('td', class_='lista-libros1'):
        for element in line.find_all('a'):
            author_key = element.get('href')
            if not author_key:
                continue
            else:
                author_list.append(author_key)

    return author_list


def main():
    web_root = 'https://albalearning.com/audiolibros/'
    authors = get_author_keywords(web_root)


if __name__ == '__main__':
    main()
Now we can use the author keywords variable(author_keywords) to create a list of links defining the sites of the authors’ books by appending author_keywords to the web_root(adding the character '/' in between to correctly set the web address) . We also set the parent directory using the os package to define the location where the sound files will be stored on your local PC.


def set_variables(web_root, author_keywords):
    abspath = os.path.abspath(__file__)
    parent_dir = os.path.dirname(abspath)
    os.chdir(parent_dir)
    user_input_urls = [web_root + elem + '/' for elem in author_keywords]
    return parent_dir, user_input_urls


Finally, we can loop over the variable url to navigate throughout the main site using the links provided by the user_input_urls list corresponding to the web addresses of the authors.


def main():
    web_root = 'https://albalearning.com/audiolibros/'
    author_keywords = get_author_keywords(web_root)
    parent_dir, user_input_urls = set_variables(web_root, author_keywords)
    for url in user_input_urls:
        raw_links = get_links(url)[0]
        links = filter_links(raw_links)


if __name__ == '__main__':
    main()
# ’ or ‘/’ (corresponding to redundant links leading to the main page or to other sections); string '-en'(english audiobooks) or string '-fr'(french audiobooks). Here below you can find the implementation of both functions:
The idea now is to create a function get_links(url) capable to extract the links on the sites of the authors to search for the mp3 files later. Following the same idea as before, we use the method .find_all() to search for the values of the href attributes from the hyperlink elements. However, now we distinguish between external links(those starting with 'http...') and internal links(the rest of links within the authors’ sites). The internal links represent the keywords to be appended to the current web address to access to the books of the corresponding author. But we need to apply filter_links()within the loop of the main()function to discard links including: characters ‘


def filter_links(links):
    # Removes links with '#', '/', '-en.' or '-fr.' to avoid unwanted links.
    regex = re.compile(r'([#/]|(-en.)|(-fr.))')
    clean_links = [link for link in links if not regex.search(link)]
    return clean_links


def get_links(url):
    website_content = requests.get(url.strip()).text
    soup = BeautifulSoup(website_content, features='html.parser')

    internal_links = set()
    external_links = set()

    # We search for the links:
    for line in soup.find_all('a'):
        link = line.get('href')
        if not link:
            continue
        if link.startswith('http'):
            external_links.add(link)
        else:
            internal_links.add(link)

    return [internal_links, external_links]


Now we simply add the code within the main loop to make the folders based on the keywords of the authors where the audiobooks will be saved(marked as bold in the code block below). Once the author folder created we just need to search for and download the mp3 files with the function download_mp3_files().


def main():
    web_root = 'https://albalearning.com/audiolibros/'
    author_keywords = get_author_keywords(web_root)
    parent_dir, user_input_urls = set_variables(web_root, author_keywords)
    for url in user_input_urls:
        links = get_links(url)[0]
        folder = author_keywords[user_input_urls.index(url)]
        file_path = os.path.join(parent_dir, folder)
        os.makedirs(file_path, exist_ok=True)
        download_mp3_files(url, links, file_path, parent_dir)


if __name__ == '__main__':
    main()
The function download_mp3_files() calls get_mp3_links() to check whether any link whose value includes the string'.mp3' exists in the current page. It is interesting to note that the filter method .find_all gives the possibility to add a function as the value of the fine-tuning parameter of interest. In this case we look for the values of the attribute src within the element source including the string'.mp3', hence the use of src = with_string to test the presence of mp3 files on the webpage using a trivial regular expression . The code is depicted below:


def get_mp3_links(mp3_url):
    website_content = requests.get(mp3_url.strip()).text
    soup = BeautifulSoup(website_content, features='html.parser')

    def with_string(src):
        return src and re.compile('.*.mp3').search(src)
    links = []
    for link in soup.find_all('source', src=with_string):
        links.append(link['src'])
    return links


def get_chapters_links(input_url, root_link):
    internal_links = get_links(input_url)[0]
    # Keeps links whose address includes the name of the requested author
    links = [link for link in internal_links if root_link in link]
    return links


def download_mp3_files(url, links, file_path, parent_dir):
    author_root = url[:url.rfind('/')+1]
    full_links = [author_root + link for link in links]
    for link in full_links:
        mp3_link = get_mp3_links(link)

    if len(mp3_link) == 0:  # no mp3 link found on this webpage
        root_link = link[link.rfind('/')+1:-5]
        new_file_path = file_path + '\\' + root_link
        os.makedirs(new_file_path, exist_ok=True)
        new_links = get_chapters_links(link, root_link)
        new_full_links = [author_root + link for link in new_links]

    for new_link in new_full_links:
        new_mp3_link = get_mp3_links(new_link)

        if len(new_mp3_link) == 0:
            print(
                f'WARNING: The address: {new_link} very likely has several chapters or a link is wrong!')
            continue

        mp3_link = new_mp3_link[0]
        doc = requests.get(mp3_link)
        filename = mp3_link[mp3_link.rfind('/')+1:]
        # To modify next line in case of different root webpage
        new_filename = filename[filename.find('/albalearning-')+14:]
        with open(new_file_path+'\\'+new_filename, 'wb') as f:
            f.write(doc.content)
    elif len(mp3_link) > 1:
        print('WARNING: More than one mp3 file have been found!')
    else:
        mp3_link = mp3_link[0]
        doc = requests.get(mp3_link)
        filename = mp3_link[mp3_link.rfind('/')+1:]
        new_filename = filename[filename.rfind('-')+1:]
        with open(file_path+'\\'+new_filename, 'wb') as f:
        f.write(doc.content)
    return None

