from operator import itemgetter

import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process the information about each submission.
submissiong_ids = r.json()
submissions_dicts = []
for submission_id in submissiong_ids[:20]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    # print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    try:
        submission_dict = {
                "title": response_dict["title"],
                "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
                "comments": response_dict["descendants"],
        }
    except KeyError:
        continue
    else:
        submissions_dicts.append(submission_dict)

submission_dicts = sorted(submissions_dicts, key=itemgetter("comments"), reverse=True)

article_links, comment_counts, hover_texts = [], [], []
for submission_dict in submission_dicts:
    title = submission_dict["title"][:30]
    discussion_link = submission_dict["hn_link"]
    article_link = f'<a href="{discussion_link}"">{title}</a>'
    comment_count = submission_dict["comments"]

    article_links.append(article_link)
    comment_counts.append(comment_count)
    hover_texts.append(submission_dict["title"])

title = "Most Commented Hacker News Articles"
labels = {
    'x': 'Article',
    'y': 'Comments count',
}

fig = px.bar(
    x = article_links,
    y = comment_counts,
    title = title,
    labels = labels,
    hover_name = hover_texts,
)

fig.update_layout(
        title_font_size = 20,
        xaxis_title_font_size = 15,
        yaxis_title_font_size = 15,
)

fig.update_traces(
    marker_color = 'SteelBlue',
    marker_opacity = 0.8,
)

fig.show()

