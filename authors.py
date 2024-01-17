## Dictionary that stores authors as keys and their respective books as values

authors_books = {'A. Einstein': ['Relativity: The Special and General Theory',
                                 'Sidelights on Relativity'],
                'J. Maxwell': ['A Treatise on Electricity and Magnetism',
                               'Theory of Heat'],
                'M. Curie': ['Radioactive Substances',
                              'Treatise on Radioactivity']}

# Print the author and then the list of books as a string
for author, books in authors_books.items():
    print(f"{author} {('  |  ').join(books)}\n")