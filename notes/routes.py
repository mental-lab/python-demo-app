import logging
from notes import db, note
from notes.forms import AddForm, DeleteForm
from flask import render_template, request, send_file, flash, redirect, jsonify


@note.route('/', methods=['GET', 'POST'])
@note.route('/index', methods=['GET', 'POST'])
def index():
    items = get_note_ui()
    arr = []
    for item in items:
        try:
            _id = item[0]
            _note = item[1]
            note_str = '%s. "%s"' % (_id, _note)
            arr.append(note_str)
        except Exception as e:
            return str(e)

    add_form = AddForm()
    delete_form = DeleteForm()

    if add_form.validate_on_submit():
        add_note(add_form.note_field.data)
        flash('Note "{}" has been added!'.format(
            add_form.note_field.data))

        return redirect('/')

    # TODO: Add return and flash error if note does not exist
    if delete_form.validate_on_submit():
        delete_note(delete_form.id_field.data)
        flash('Note "{}" has been Deleted!'.format(
            delete_form.id_field.data))

        return redirect('/')
    
    return render_template('index.html', notes=arr, add_form=add_form, delete_form=delete_form)


@note.route('/add', methods=['POST'])
def add_note(msg=""):

    if not msg:
        data = request.get_json(force=True)
        msg = data.get('message')

    if not msg:
         return jsonify({"Error": "No message in Request"}), 400

    if len(msg) > 1024:
        return jsonify({"Error": "Message tooooo long!"}), 400

    if (msg == "\""):
        response = jsonify({"Sucess": "Maybe a Security Issue!"})
        response.headers.set('Content-Type', 'text/html')
        return response, 200

    conn = db.create_connection()
    with conn:
        try:
            db.create_note(conn, (str(msg),))
            return jsonify({"Sucess": "Note added!"})
        except Exception as e:
            err = "%s" % e
            return jsonify({"Error": err}), 500


@note.route('/delete', methods=['DELETE'])
def delete_note(id=None):
    if not id:
        id = request.args.get('id')

    if not id:
        return "No Id sent in request."

    conn = db.create_connection()
    with conn:
        try:
            db.delete_note(conn, id)
            return "Note deleted successfully!"
        except Exception as e:
            return "Failed to delete Note: %s" % e

def get_note_ui():
    id = request.args.get('id')
    conn = db.create_connection()

    with conn:
        try:
            return db.select_note_by_id(conn, id)
        except Exception as e:
            return "Failed to delete Note: %s" % e

@note.route('/get', methods=['GET'])
def get_note():
    return str(get_note_ui())
