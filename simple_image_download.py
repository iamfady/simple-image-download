from simple_image_download import simple_image_download as simp # type: ignore


response = simp.simple_image_download

keywords = ["strawberry"]

for kw in keywords:
    response().download(kw, 300) 
