import requests
import json
from flask import Flask, jsonify, redirect, url_for, request, session, make_response

from flask_cors import CORS


app = Flask(__name__)
CORS(app)

filename = "bookofmormon.json"
file = open(filename, "r")
book_of_mormon_in_memory = json.loads(file.read())

BOOK_CHAPTERS = [ {'book':book['book'],'chapters':len(book['chapters'])} for book in book_of_mormon_in_memory['books']]

BOOK_INDEXS = len(BOOK_CHAPTERS)

FULL_CHAPTERS = [ {'book':book['book'],'chapters':len(book['chapters'])} for book in book_of_mormon_in_memory['books']]

def getVerses():
	verses = []
	for book_obj in book_of_mormon_in_memory['books']:
		for chapter in book_obj['chapters']:
			for verse in chapter['verses']:
				verses.append(verse)
	return verses

VERSES = getVerses()

def getChapter(bookname,chapter):
	for book_obj in book_of_mormon_in_memory['books']:
		if book_obj['book'] == bookname:
			chapters_len = len(book_obj['chapters'])
			if chapter <= chapters_len:
				return book_obj['chapters'][chapter - 1]


@app.route('/all', methods=('GET', 'POST'))
def all():
	return make_response(jsonify([book for book in book_of_mormon_in_memory['books']]), 200, {})

@app.route('/books', methods=('GET', 'POST'))
def books():
	return make_response(jsonify(BOOK_CHAPTERS), 200, {})

@app.route('/<book>/<int:chapter>', methods=('GET', 'POST'))
def book_chapter(book,chapter):
	return make_response(jsonify(getChapter(book,chapter)), 200, {})

@app.route('/<ref>', methods=('GET', 'POST'))
def get_ref(ref):
	for verse in VERSES:
		if verse['reference'].lower() == ref.lower():
			return make_response(jsonify(verse), 200, {})
	

	




if __name__ == '__main__':
	app.run(debug=True)


    
    
    
    
