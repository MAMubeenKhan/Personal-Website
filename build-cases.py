"""
One-off generator for the case-study pages.

Writes plain static HTML into work/. Run it once; after that you can edit the
generated files directly and never touch this script again. It exists so the
seven pages start out structurally identical, not to become a build step.

    python build-cases.py
"""

import io
import os

EMAIL = "mamubeenkhan@gmail.com"
WHATSAPP = "918328681249"
UPWORK = "https://www.upwork.com/freelancers/~01b1a4192e5a8aa284"

CASES = [
    {
        "slug": "spendpedia",
        "name": "Spendpedia",
        "kind": "Personal finance · Android",
        "icon": "spendpedia-icon.png",
        "status": ("live", "Live on Google Play"),
        "summary": "An expense tracker built around the thing that kills every "
                   "expense tracker: nobody wants to type in what they just spent.",
        "facts": [
            ("Platform", "Android 7.0+, iOS in progress"),
            ("Stack", "Flutter, cloud sync, LLM categorisation"),
            ("Role", "Everything — design, build, store listing, submission"),
            ("Model", "Free tier, premium subscription, 7-day trial"),
        ],
        "links": [("Google Play", "https://play.google.com/store/apps/details?id=com.spendpedia.app"),
                  ("spendpedia.com", "https://spendpedia.com")],
        "shots": ["spendpedia-1.jpg", "spendpedia-3.jpg", "spendpedia-4.jpg", "spendpedia-6.jpg"],
        "problem": [
            "Almost everyone has installed a budgeting app and stopped using it "
            "within two weeks. The reason is never the charts. It is that "
            "logging a coffee takes six taps, and after the fourth day you stop "
            "bothering — and an expense tracker with four days of data in it is "
            "worse than none, because it tells you a confidently wrong story.",
            "So the design problem was not analytics. It was reducing the cost "
            "of entering a single expense to almost nothing.",
        ],
        "built": [
            "<strong>Voice entry with AI categorisation.</strong> Say what you "
            "spent and the app parses the amount, guesses the category and files "
            "it. The LLM only handles the messy part — turning free speech into "
            "structured fields — while the arithmetic stays ordinary code, "
            "because a language model should never be the thing adding up "
            "someone's money.",
            "<strong>Budgets that speak up.</strong> Monthly limits per category "
            "with alerts as you approach them, rather than a report at month end "
            "telling you what you already cannot change.",
            "<strong>Analytics worth opening.</strong> Category breakdowns and "
            "spending patterns over time, which is what turns logging into a "
            "habit that pays back.",
            "<strong>Your data stays yours.</strong> Encrypted cloud sync across "
            "devices, full offline operation, and export to CSV or PDF. No ads.",
        ],
        "hard": [
            "Financial apps get the strictest treatment on Google Play. The "
            "data-safety declaration has to match what the app actually does, "
            "field by field, and a mismatch between the form and the binary is a "
            "rejection rather than a question.",
            "Offline-first sync is the part people underestimate. The app has to "
            "work fully with no connection and then reconcile without ever "
            "silently losing or duplicating an entry — because in a finance app, "
            "a duplicated entry is not a bug, it is a wrong number the user "
            "trusts.",
        ],
        "now": "Live on Google Play with a free tier and a premium subscription. "
               "The iOS build is in progress. The site carries a budget "
               "calculator and a set of personal-finance articles, both aimed at "
               "search traffic rather than at existing users.",
    },
    {
        "slug": "hushthem",
        "name": "HushThem",
        "kind": "Call control · Android",
        "icon": "hushthem-icon.png",
        "status": ("live", "Live on Google Play"),
        "summary": "Spam-call blockers play catch-up with a list that never ends. "
                   "This one inverts it: nobody rings unless you said they could.",
        "facts": [
            ("Platform", "Android 10+"),
            ("Stack", "Flutter, Android telephony APIs"),
            ("Role", "Everything — design, build, permissions review, submission"),
            ("Model", "Free"),
        ],
        "links": [("Google Play", "https://play.google.com/store/apps/details?id=com.hushthem.app"),
                  ("hushthem.com", "https://hushthem.com")],
        "shots": [],
        "problem": [
            "Every call blocker works the same way: a blocklist of known spam "
            "numbers that grows forever and is always one step behind, because "
            "the next call comes from a number nobody has reported yet.",
            "But most people do not want to block a list. They want the opposite "
            "— during a meeting, a shift, or the night, they want the phone "
            "silent for everyone except a handful of people who genuinely "
            "matter.",
        ],
        "built": [
            "<strong>Whitelist-first.</strong> Pick who is allowed through. "
            "Everyone else is silenced or auto-rejected, your choice. There is "
            "no list to maintain and no catching up to do.",
            "<strong>Night mode.</strong> Stricter blocking on a schedule, so "
            "the setting does not have to be remembered at bedtime.",
            "<strong>Call analytics.</strong> What was blocked and what was "
            "missed, so the app can be trusted rather than just believed — "
            "anyone handing over their calls wants to verify nothing important "
            "vanished.",
            "<strong>Nothing leaves the phone.</strong> All data stays on the "
            "device, with an optional biometric lock.",
        ],
        "hard": [
            "Call and phone-state permissions are among the most restricted on "
            "Google Play. Requesting them means declaring exactly why, "
            "demonstrating the core function genuinely requires them, and "
            "accepting that a weak justification is rejected outright. Plenty of "
            "call apps never make it out of that queue.",
            "Getting silencing to behave identically across Android versions and "
            "manufacturer skins is unglamorous, fiddly work, and it is the "
            "difference between an app that works and one that works on the "
            "developer's own phone.",
        ],
        "now": "Live on Google Play, free, on Android 10 and up. There is a "
               "partner programme on the site for anyone who wants to promote it.",
    },
    {
        "slug": "flaris",
        "name": "Flaris",
        "kind": "AR beauty · Android",
        "icon": "flaris-icon.png",
        "status": ("live", "Live on Google Play"),
        "summary": "Augmented-reality makeup try-on with over 700 guided looks — "
                   "and no brand telling you what to buy.",
        "facts": [
            ("Platform", "Android, iOS in progress"),
            ("Stack", "Flutter, real-time AR face tracking"),
            ("Role", "Everything — design, build, content structure, submission"),
            ("Model", "Free with premium features"),
        ],
        "links": [("Google Play", "https://play.google.com/store/apps/details?id=com.flaris.app"),
                  ("flaris.beauty", "https://flaris.beauty")],
        "shots": ["flaris-shot.png"],
        "problem": [
            "Makeup try-on already exists — but nearly all of it is built by "
            "brands, and it exists to sell you that brand's products. Point it "
            "at your face and the answer is always a shade you have to buy.",
            "Meanwhile the actual difficulty is technique. A tutorial shows the "
            "look on someone else's face, at someone else's skill level, and "
            "leaves you to work out the rest.",
        ],
        "built": [
            "<strong>AR try-on per procedure.</strong> Not one finished look "
            "stamped onto your face, but each individual step, so you can see "
            "what a technique does before attempting it.",
            "<strong>Over 700 guided looks and procedures</strong>, with "
            "step-by-step instructions rather than a filtered result.",
            "<strong>Brand-agnostic.</strong> It works with whatever you already "
            "own, which is the whole reason it can be honest about technique.",
            "<strong>Personalised</strong> to skin tone, face shape and style, "
            "with favourites for the looks you return to.",
        ],
        "hard": [
            "Real-time face tracking has to hold a steady frame rate on "
            "mid-range Android hardware, which is what most of the audience "
            "actually owns. Fast on a flagship is not a result.",
            "Camera permission on a beauty app invites suspicion, fairly. The "
            "data-safety declaration and privacy policy had to be unambiguous "
            "about what the camera feed is and is not used for.",
        ],
        "now": "Live on Google Play. The iOS build is in progress. The site "
               "carries a blog and support material.",
    },
    {
        "slug": "cuepaste",
        "name": "CuePaste",
        "kind": "Productivity · Windows",
        "icon": "cuepaste-icon.png",
        "status": ("live", "Live on Microsoft Store"),
        "summary": "A sequential clipboard queue. Copy five things in order, "
                   "paste them back one at a time, in that order.",
        "facts": [
            ("Platform", "Windows 10 and 11"),
            ("Stack", "Windows desktop, MSIX packaging"),
            ("Role", "Everything — design, build, packaging, certification"),
            ("Model", "Microsoft Store"),
        ],
        "links": [("Microsoft Store", "https://apps.microsoft.com/detail/9p1tsjklw82w")],
        "shots": ["cuepaste-1.jpg", "cuepaste-2.jpg"],
        "problem": [
            "Moving several pieces of information between two windows means "
            "alt-tabbing once per item: copy, switch, paste, switch back, copy "
            "the next. Filling a form from a document, or moving fields between "
            "two systems, turns into dozens of pointless context switches.",
            "Clipboard history managers exist, but they solve a different "
            "problem — they let you hunt back through what you copied. Nobody "
            "wants to hunt. You already know the order.",
        ],
        "built": [
            "<strong>A queue, not a history.</strong> Copy several items and they "
            "line up. Each paste takes the next one. The order you copied is the "
            "order you get back.",
            "<strong>Stays out of the way.</strong> It is a small utility that "
            "sits behind the keyboard shortcuts you already use, rather than an "
            "app you open.",
        ],
        "hard": [
            "Microsoft Store certification is a different discipline from Google "
            "Play — MSIX packaging, identity, capability declarations, and a "
            "certification pass that fails on details a web developer never "
            "encounters.",
            "Clipboard interception has to be careful. It sits in the path of "
            "everything a user copies, including passwords, so the correct "
            "behaviour is to hold as little as possible for as short a time as "
            "possible.",
        ],
        "now": "Live on the Microsoft Store for Windows 10 and 11.",
    },
    {
        "slug": "riverside-files",
        "name": "Riverside Files",
        "kind": "Idle tycoon game · Android",
        "icon": None,
        "mono": "RF",
        "status": ("pending", "In review for production"),
        "summary": "An idle detective-agency tycoon. Hire investigators, take "
                   "cases, grow the agency — and keep earning while the app is "
                   "shut.",
        "facts": [
            ("Platform", "Android, iOS planned"),
            ("Stack", "Flutter"),
            ("Role", "Everything — design, systems, balancing, build"),
            ("Status", "Awaiting production access on Google Play"),
        ],
        "links": [],
        "shots": [],
        "problem": [
            "Idle games look simple and are the opposite. The genre lives or "
            "dies on an economy that stays interesting for weeks — fast enough "
            "in the first ten minutes that a player comes back tomorrow, slow "
            "enough at hour twenty that progress still means something.",
            "The detective-agency setting gives that curve a reason to exist: "
            "cases, investigators and an agency that grows are a natural fit for "
            "hiring, upgrading and unlocking.",
        ],
        "built": [
            "<strong>An idle economy that runs while closed.</strong> Offline "
            "progression has to be computed on return rather than simulated "
            "tick by tick — get it wrong and players either lose earnings they "
            "were promised or find an exploit and stop playing.",
            "<strong>Agency progression.</strong> Investigators to hire, cases "
            "to take, upgrades that change the shape of the curve rather than "
            "just multiplying it.",
            "<strong>Built in Flutter</strong>, same as the rest of my mobile "
            "work, which is how a solo developer ships a game and three utility "
            "apps without maintaining separate toolchains.",
        ],
        "hard": [
            "Balancing is the whole job. Every number interacts with every other "
            "number, and the only honest way to tune it is to play it, "
            "repeatedly, at different stages.",
            "Google Play now requires new personal developer accounts to run a "
            "closed test before production access is granted. That is a real "
            "gate with real testers and a real waiting period, and it is where "
            "the game currently sits.",
        ],
        "now": "In review for production access on Google Play.",
    },
    {
        "slug": "gym-management",
        "name": "Gym management system",
        "kind": "Client work · Windows desktop",
        "icon": None,
        "mono": "GM",
        "status": ("pending", "In delivery"),
        "summary": "Members, plans, attendance and billing for a working gym. "
                   "Built to a paying client's brief.",
        "facts": [
            ("Platform", "Windows desktop"),
            ("Client", "Confidential"),
            ("Role", "Sole developer — requirements, build, delivery"),
            ("Status", "In delivery"),
        ],
        "links": [],
        "shots": [],
        "problem": [
            "A gym runs on membership dates, plan renewals and who walked in "
            "today. Handled on paper or in a spreadsheet, the failure is always "
            "the same: renewals get missed, and a missed renewal is revenue that "
            "simply never arrives.",
            "Off-the-shelf gym software is mostly cloud subscriptions built for "
            "chains, priced per location, and useless the moment the internet at "
            "the front desk goes down.",
        ],
        "built": [
            "<strong>Member and plan management</strong> — the record of who is "
            "on what plan and when it ends, which is the thing the whole "
            "business actually runs on.",
            "<strong>Attendance</strong>, captured at the desk in the few "
            "seconds a member is standing there. If check-in is slow, staff stop "
            "doing it and the data dies.",
            "<strong>Billing and renewals</strong>, so a lapse is visible before "
            "it becomes a lost member rather than after.",
            "<strong>Runs offline on the machine at the desk.</strong> No "
            "connection required to sign someone in.",
        ],
        "hard": [
            "Client software is a different job from your own product. The brief "
            "comes from how the gym already works, not from what would be "
            "elegant, and the software has to fit the staff rather than retrain "
            "them.",
            "The client's name stays confidential until they are happy to be "
            "named. Happy to walk through the system in a call.",
        ],
        "now": "In delivery to the client. Once it is handed over, I intend to "
               "build the same system out as a hosted product for independent "
               "gyms — the problem is identical everywhere and the existing "
               "options are priced for chains.",
    },
    {
        "slug": "adlib",
        "name": "AdLib",
        "kind": "Chrome extension · MV3",
        "icon": "adlib-icon.png",
        "status": ("pending", "In store review"),
        "summary": "Makes Meta's Ad Library usable — sortable, filterable, "
                   "exportable. The most technically demanding thing on this site.",
        "facts": [
            ("Platform", "Chrome, Manifest V3"),
            ("Stack", "TypeScript, React, Vite, CRXJS"),
            ("Role", "Everything — research, build, store submission"),
            ("Status", "In Chrome Web Store review"),
        ],
        "links": [],
        "shots": [],
        "problem": [
            "Meta's Ad Library holds every ad running on Facebook and Instagram "
            "and is close to unusable. You cannot sort it. You cannot filter it "
            "properly. You cannot export it. Finding which of an advertiser's "
            "two thousand ads has been running longest means scrolling, by hand, "
            "for a very long time.",
            "Every commercial tool in this space solves it by scraping Meta from "
            "their own servers. That is the easy path and it is the one I "
            "deliberately did not take.",
        ],
        "built": [
            "<strong>Everything happens in the user's own browser.</strong> The "
            "extension reads the data the page has already loaded on the user's "
            "own session. No server ever contacts Meta. That is a legal posture, "
            "chosen up front, and the architecture is built around it rather "
            "than bolted on.",
            "<strong>Sort, filter, search</strong> across an advertiser's entire "
            "catalogue, including sorting by how long an ad has been running — "
            "the signal that actually indicates a competitor is spending money.",
            "<strong>Creative reuse detection</strong> — which creatives appear "
            "in more than one ad set, which is how you tell what is being "
            "scaled from what is being tested.",
            "<strong>CSV export and bulk media download</strong>, throttled "
            "deliberately, because the requests are spent on the user's own "
            "session and a rate-limited account is a lost customer.",
        ],
        "hard": [
            "The data comes from intercepting the page's own GraphQL responses, "
            "which means running code in two isolated JavaScript contexts and "
            "bridging them, with reconciliation counters so a dropped message "
            "can never look like an advertiser simply having fewer ads.",
            "Meta's field names change without warning. Every one of them is "
            "quarantined in a single adapter file, and an 878-case fixture suite "
            "built from real captured traffic gates every change — so when the "
            "schema drifts, exactly one file needs editing and the tests say "
            "which line.",
            "One measurement changed the whole product. Reach data exists only "
            "in a per-ad request, one ad at a time, so bulk reach estimation is "
            "not honestly possible on a user's own session. I measured that "
            "before building the feature and cut it, rather than shipping a "
            "number I could not stand behind.",
        ],
        "now": "In review at the Chrome Web Store, launching free.",
    },
]


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} — Mubeen Khan</title>
<meta name="description" content="{summary_plain}">
<meta property="og:title" content="{name} — Mubeen Khan">
<meta property="og:description" content="{summary_plain}">
<link rel="icon" href="../images/apps/adlib-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../style.css">
</head>
<body>

<header class="site-head">
  <div class="wrap">
    <a class="brand" href="../index.html">Mubeen Khan<span>.</span></a>
    <nav class="nav">
      <a href="../index.html#work">Work</a>
      <a class="only-wide" href="../index.html#services">Services</a>
      <a href="../index.html#contact">Contact</a>
    </nav>
  </div>
</header>

<main class="wrap">

  <div class="case-head">
    <a class="back" href="../index.html#work">← All work</a>
    <div class="card-top">
      {iconhtml}
      <div>
        <h3 style="font-size:1rem;color:var(--ink-faint);font-weight:500;margin:0">{kind}</h3>
      </div>
    </div>
    <h1>{name}</h1>
    <p class="lead">{summary}</p>
    <p><span class="pill {pillclass}">{statuslabel}</span></p>
    {linkshtml}
  </div>

  <div class="facts">
{factshtml}
  </div>

  {shotshtml}

  <div class="prose">
    <h2>The problem</h2>
{problem}

    <h2>What I built</h2>
    <ul>
{built}
    </ul>

    <h2>The part that was actually hard</h2>
{hard}

    <h2>Where it is now</h2>
    <p>{now}</p>
  </div>

  <div class="next">
    <p class="eyebrow">Next</p>
    <h2 style="margin-bottom:18px"><a href="{nextslug}.html" style="text-decoration:none">{nextname} →</a></h2>
    <p class="lead" style="margin-bottom:26px">Or tell me what you want built.</p>
    <div class="contact-actions" style="margin:0">
      <a class="btn btn-primary" href="mailto:{email}?subject=Project%20enquiry">Email me</a>
      <a class="btn btn-line" href="https://wa.me/{whatsapp}" target="_blank" rel="noopener">WhatsApp</a>
    </div>
  </div>

</main>

<footer class="site-foot">
  <div class="wrap">
    <div class="foot-row">
      <a href="../index.html#work">Work</a>
      <a href="../index.html#services">Services</a>
      <a href="../index.html#contact">Contact</a>
      <a href="https://github.com/MAMubeenKhan" target="_blank" rel="noopener">GitHub</a>
    </div>
    <p style="margin:0">© <span id="yr">2026</span> Mohammed Abdul Mubeen Khan</p>
  </div>
</footer>

<div class="bar">
  <a class="btn btn-line" href="https://wa.me/{whatsapp}" target="_blank" rel="noopener">WhatsApp</a>
  <a class="btn btn-primary" href="mailto:{email}?subject=Project%20enquiry">Email me</a>
</div>

<script>document.getElementById("yr").textContent = new Date().getFullYear();</script>
</body>
</html>
"""


def strip_tags(text):
    out, depth = [], 0
    for ch in text:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        elif depth == 0:
            out.append(ch)
    return "".join(out)


def build():
    os.makedirs("work", exist_ok=True)

    for i, c in enumerate(CASES):
        nxt = CASES[(i + 1) % len(CASES)]

        if c.get("icon"):
            iconhtml = ('<img class="app-icon" src="../images/apps/%s" alt="" '
                        'width="64" height="64">' % c["icon"])
        else:
            iconhtml = ('<div class="app-icon mono" aria-hidden="true">%s</div>'
                        % c.get("mono", "?"))

        links = "".join(
            '<a class="btn btn-line" href="%s" target="_blank" rel="noopener">%s ↗</a>'
            % (url, label) for label, url in c["links"]
        )
        linkshtml = '<div class="case-links">%s</div>' % links if links else ""

        factshtml = "\n".join(
            '    <div><b>%s</b><span>%s</span></div>' % (k, v) for k, v in c["facts"]
        )

        if c["shots"]:
            imgs = "".join(
                '<img src="../images/apps/%s" alt="%s screenshot" loading="lazy">'
                % (s, c["name"]) for s in c["shots"]
            )
            shotshtml = '<div class="shots">%s</div>' % imgs
        else:
            shotshtml = ""

        html = PAGE.format(
            name=c["name"],
            kind=c["kind"],
            summary=c["summary"],
            summary_plain=strip_tags(c["summary"]).replace('"', "'"),
            iconhtml=iconhtml,
            pillclass="pill-live" if c["status"][0] == "live" else "",
            statuslabel=c["status"][1],
            linkshtml=linkshtml,
            factshtml=factshtml,
            shotshtml=shotshtml,
            problem="\n".join("    <p>%s</p>" % p for p in c["problem"]),
            built="\n".join("      <li>%s</li>" % b for b in c["built"]),
            hard="\n".join("    <p>%s</p>" % h for h in c["hard"]),
            now=c["now"],
            nextslug=nxt["slug"],
            nextname=nxt["name"],
            email=EMAIL,
            whatsapp=WHATSAPP,
        )

        path = os.path.join("work", c["slug"] + ".html")
        io.open(path, "w", encoding="utf-8", newline="\n").write(html)
        print("wrote", path)


if __name__ == "__main__":
    build()
