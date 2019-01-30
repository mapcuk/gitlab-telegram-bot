import os
import json

os.environ['SOCKS_PROXY'] = 'socks5://my-proxy.com:5000'
os.environ['AUTHMSG'] = 'hello'
os.environ['TELEGRAM_TOKEN'] = 'secret token'

from app import generatePipelineMsg, generateCommentMsg


def test_pipeline_message():
    pipeline_data = json.load(open('samples/webhook-pipeline.json', 'r'))
    message = generatePipelineMsg(pipeline_data)
    print(message)
    assert len(message) > 10
    assert 'branch' in message


def test_note_message():
    note_data = json.load(open('samples/webhook-note.json', 'r'))
    message = generateCommentMsg(note_data)
    print(message)
