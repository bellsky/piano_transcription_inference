import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piano-transcription-bellsky", # Replace with your own username
    version="0.0.51",
    author="Qiuqiang Kong",
    author_email="always1skyg@gmail.com",
    description="Piano transcription inference toolbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bellsky/piano_transcription_inference",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['matplotlib', 'mido', 'librosa>=0.9.0', 'torchlibrosa'],
    python_requires='>=3.6',
)
