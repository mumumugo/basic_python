from indeed import extract_indeed_pages,extract_indeed_jobs

#max_indeed_pages = extract_indeed_pages()
#print(max_indeed_pages)

last_indeed_page = extract_indeed_pages()
extract_indeed_jobs(last_indeed_page)
