from instaloader import Instaloader, Profile
L = Instaloader()
Pro = "mozillassgmce"
profile = Profile.from_username(L.context, Pro)
post = profile.get_posts()
for p in post:
    L.download_post(Pro, p)
