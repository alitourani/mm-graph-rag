from setuptools import find_packages, setup


def parseRequirements(filename):
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
    reqs = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            reqs.append(line)
    return reqs


with open("README.md", encoding="utf-8") as readme_file:
    long_description = readme_file.read()


setup(
    version="1.0.0",
    name="MM-Graph-RAG",
    author="Ali Tourani",
    maintainer='Ali Tourani',
    python_requires=">=3.12",
    include_package_data=True,
    long_description=long_description,
    author_email="a.tourani1991@gmail.com",
    long_description_content_type="text/markdown",
    url="https://github.com/alitourani/mm-graph-rag",
    description="A Graph-based, Multi-Modal RAG System",
    packages=find_packages(include=["mm_graph_rag", "mm_graph_rag.*"], exclude=['docs', 'examples', 'rtd']),
    entry_points={
        'console_scripts': ['blenderproc=blenderproc.command_line:cli'],
    },
    install_requires=parseRequirements("requirements.txt"),
)