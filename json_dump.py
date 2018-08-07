import io
import json


def dump_to_json(data):
    with io.open(data, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, f, ensure_ascii=False))
