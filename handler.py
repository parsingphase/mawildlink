redirects = [
    ["group", "Facebook Group", "https://www.facebook.com/groups/MAWildlife"],
    ["rules", "Facebook Group Rules",
     "https://www.facebook.com/notes/massachusetts-wildlife/massachusetts-wildlife-rules-details/3045269308934439/"],
    ["faq", "Group FAQ",
     "https://www.facebook.com/notes/massachusetts-wildlife/massachusetts-wildlife-faq/306350497440553/"],
    ["pinned", "Group Pinned Post", "https://www.facebook.com/groups/MAWildlife/permalink/649606069019913/"],
    ["philosophy", "Moderation Philosophy",
     "https://www.facebook.com/notes/massachusetts-wildlife/moderation-philosophy-for-massachusetts-wildlife/753679958712237/"],
    ["dslrwild", "Guide to DSLR photography",
     "https://parsingphase.medium.com/some-notes-on-wildlife-photography-6370ea4f8965"]
]


def redirect(event, context):
    response = None

    if "rawPath" in event:
        stub = event["rawPath"].lstrip('/')
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
                for l in redirects
            ]
        )

        response = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/html; charset=utf-8"
            },
            "body": f'<p>Link not found. Available options:</p><ul>{link_list}</ul>'
        }

    return response
