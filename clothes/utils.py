def setup_cloudinary() -> None:
    from dotenv import load_dotenv

    load_dotenv()
    import cloudinary

    config = cloudinary.config(secure=True)


setup_cloudinary()


def uploadImage(image, name: str):
    import cloudinary
    from cloudinary.uploader import upload

    upload(image, public_id=name, unique_filename=False, overwrite=True)
    return cloudinary.CloudinaryImage(name).build_url()
