from youtubesearchpython import VideosSearch
import webbrowser

def search_and_play_youtube(query, limit=1):
    videosSearch = VideosSearch(query, limit=limit)
    results = videosSearch.result()
    if results and 'result' in results and len(results['result']) > 0:
        first_result = results['result'][0]
        video_link = first_result['link']
        print(f"Opening: {video_link}")
        webbrowser.open(video_link)
    else:
        print("No results found.")

search_query = input("Enter the search query: ")

search_and_play_youtube(search_query)
