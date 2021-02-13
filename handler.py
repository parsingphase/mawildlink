redirects = [
    ["welcome", "Facebook Group Welcome Post",
     "https://www.facebook.com/notes/massachusetts-wildlife/welcome-to-the-massachusetts-wildlife-group/1351087361921547/"],
    ["fb", "Facebook Group", "https://www.facebook.com/groups/MAWildlife"],
    ["about", "Facebook 'About' page with short-form rules", "https://www.facebook.com/groups/MAWildlife/about"],
    ["rules", "Facebook Group Full Rules",
     "https://www.facebook.com/notes/massachusetts-wildlife/massachusetts-wildlife-rules-details/3045269308934439/"],
    ["rulesdetails", None,
     "https://www.facebook.com/notes/massachusetts-wildlife/massachusetts-wildlife-rules-details/3045269308934439/"],
    ["faq", "Group FAQ",
     "https://www.facebook.com/notes/massachusetts-wildlife/massachusetts-wildlife-faq/306350497440553/"],
    ["owls", "Owl Observation Policy",
     "https://www.facebook.com/notes/massachusetts-wildlife/massachusetts-wildlife-owl-observation-policy/845927992925738/"],
    ["care", "Vulnerable / Injured Animal Guidance",
     "https://www.facebook.com/notes/massachusetts-wildlife/concerned-about-an-animal-massachusetts-wildlife-notes/606931346466734/"],
    ["cares", None,
     "https://www.facebook.com/notes/massachusetts-wildlife/concerned-about-an-animal-massachusetts-wildlife-notes/606931346466734/"],
    ["mawildcares", None,
     "https://www.facebook.com/notes/massachusetts-wildlife/concerned-about-an-animal-massachusetts-wildlife-notes/606931346466734/"],
    ["carepdf", "Vulnerable / Injured Animal Guidance, public PDF version",
     "https://www.dropbox.com/s/0atgonhehc960mz/MAwildGuide.pdf"],
    ["announce", "Group Announcements",
     "https://www.facebook.com/groups/MAWildlife/announcements"],
    ["philosophy", None,
     "https://www.facebook.com/notes/massachusetts-wildlife/moderation-philosophy-for-massachusetts-wildlife/753679958712237/"],
    ["dslrwild", "Guide To DSLR Photography (by an admin, public)",
     "https://parsingphase.medium.com/some-notes-on-wildlife-photography-6370ea4f8965"],
    ["moderateyournope", "Phobia Handling Request",
     "https://www.facebook.com/groups/MAWildlife/permalink/675710319742821/"],
    ["pinned", None, "https://www.facebook.com/groups/MAWildlife/permalink/649606069019913/"],
    ["members", "Group Members and Administration Team", "https://www.facebook.com/groups/MAWildlife/members"]
]

header = """<!doctype html>
<html lang="en"><head><title>mawild.link</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous" />
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css" integrity="sha384-oS3vJWv+0UjzBfQzYUhtDYW+Pj2yciDJxpsK1OYPAYjqT085Qq/1cq5FLXAZQ7Ay" crossorigin="anonymous">
<style type="text/css">
 a { color: #777; text-decoration: underline; text-decoration-style: dotted; }
 a:hover { color: #444; text-decoration-style: solid }
</style>
</head>
<body><div class="container">
<h1>mawild.link redirection service</h1>
<p>This is a link-shortening service for the Massachusetts Wildlife Facebook Group,
 from the <a href="http://mawildlifecollective.com">Massachusetts Wildlife Collective</a></p>
"""

footer = """</div>
    <footer class="footer" 
    style="position: absolute; bottom: 0; width: 100%; margin-top: 20px; height: 56px;line-height: 56px;">
        <div class="container-fluid">
            <div class="gh-link" style=" padding-right: 4px; float: right"><a
                    class="text-dark" href="https://github.com/parsingphase/mawildlink"><i
                    class="fab fa-github"></i></a></div>
            <div style="float: right; padding-right: 16px;">
                mawild.link created by <a class="text-dark" href="https://parsingphase.dev">parsingphase</a>
            </div>
        </div>
    </footer>
</body></html>"""


def redirect(event, context):
    response = None
    stub = None

    if "rawPath" in event:
        stub = event["rawPath"].lstrip('/').lower()
        for link in redirects:
            if link[0] == stub:
                response = {
                    "statusCode": 302,
                    "headers": {
                        "Location": link[2]
                    },
                    "body": f"Redirecting to {link[2]}"
                }
                break

    if response is None:
        link_list = "\n".join(
            [
                f'<li>{l[1]}: <a href="/{l[0]}">mawild.link/{l[0]}</a></li>'
                for l in redirects if l[1] is not None
            ]
        )

        message = '' if stub is None or stub == '' \
            else f'<div class="alert alert-warning" role="alert">The short link <code>mawild.link/{stub}</code> was not found</div>'

        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/html; charset=utf-8"
            },
            "body": f'{header}{message}<ul>{link_list}</ul>'
                    '<p>Note that most links will require you to be a group member</p>'
                    f'{footer}'
        }

    return response


if __name__ == '__main__':
    print(redirect({}, {})['body'])
