from app import db
from app.api import bp
from app.api.auth import token_auth
from flask import request, jsonify, g, current_app
from conversation.mind import Mind
from app.models import Conversation, Utterance


# TODO: test this then factor out logic shared with
# routes. It might be that Mind should be asked if the contents have
# changed, then the new code (in operations?) should call
# sqlalchemy.orm.attributes.flag_modified(conversation, context)
@bp.route('/utterances', methods=['POST'])
@token_auth.login_required
def post_utterance():
    data = request.get_json() or {}
    for field in ['conversation_id', 'speaker_id', 'text']:
        if field not in data:
            return bad_request('missing one or more fields')
    conversation = Conversation.query.get(data['conversation_id'])
    if not conversation:
        return error_response(404, 'no such conversation')
    utterance = Utterance(speaker_id=data['speaker_id'], text=data['text'])
    conversation.add_utterance(utterance)
    source_path = current_app.config['SOURCE_PATH']
    Mind().continue_conversation(conversation, source_path)
    db.session.commit()
    return jsonify(conversation.to_dict())

