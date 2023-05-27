from flask import Blueprint,render_template,request,flash,jsonify
from flask_login import login_required,current_user
from .model import Note
from. import db
import json



views = Blueprint('views',__name__) 

# Home page only accessible for logged in users
#for adding new notes to the user
@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note=request.form.get('note')
        if len(note) <1:
            flash('Note is too short',category='errormessage')
        else:
            new_note=Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            
            flash('Note added',category='successmessage')

    return render_template('home.html',user=current_user)

# Deletes the note returns empty json
@views.route('/delete-note',methods=['POST'])
def delete_note():
    maindata=request.data.decode()
    data=json.loads(maindata)
    noteId=data['noteId']
    note=Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note deleted',category='successmessage')
    return jsonify({})