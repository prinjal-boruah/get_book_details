import requests
import xmltodict

input_url = input('Enter a Goodreads Book URL : ').strip()

def get_book_details(input_url):

    book_id = input_url.split('/')[-1].split('-')[0]

    url = f"https://www.goodreads.com/book/show/{book_id}.xml?key=Bk8NPBaKFSAlqPjOYdeJ1w"
    r = requests.get(url = url)
    if r.status_code == 404:
        return "Page not Found - Please enter a valid URL"
    xml_data = r.content #to get the xml data
    dict_data = xmltodict.parse(xml_data) #to conver the xml data to dictionary format

    title = dict_data['GoodreadsResponse']['book']['title']
    avg_rating = dict_data['GoodreadsResponse']['book']['average_rating']
    ratings_count = dict_data['GoodreadsResponse']['book']['work']['ratings_count']['#text']
    num_pages =  dict_data['GoodreadsResponse']['book']['num_pages']
    image_url =  dict_data['GoodreadsResponse']['book']['image_url']
    publication_year =  dict_data['GoodreadsResponse']['book']['work']['original_publication_year']['#text']
    author =  dict_data['GoodreadsResponse']['book']['authors']['author']['name']

    #converting strings to integers,float where it is required
    if avg_rating is not None:
        avg_rating = float(avg_rating)
    if ratings_count is not None:
        ratings_count = int(ratings_count)
    if num_pages is not None:
        num_pages = int(num_pages)

    #saving all data to a dictionary
    book_info = {
        "title": title,
        "average_rating": avg_rating,
        "ratings_count": ratings_count,
        "num_pages": num_pages,
        "image_url": image_url,
        "publication_year": publication_year,
        "authors":author,
    }

    return book_info

#to call the function with input
print(get_book_details(input_url))
