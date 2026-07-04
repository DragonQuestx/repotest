# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: JobSearch
class TagManager:
    def __init__(self, db):
        self.db = db
    
    def add_tag(self, tag_name):
        if not tag_name.strip(): return False
        existing_tags = set(tag['name'].strip().lower() for tag in self.db.get('tags', []))
        if tag_name.strip().lower() in existing_tags: return False
        new_id = max((tag['id'] for tag in self.db.get('tags', [])), default=0) + 1
        self.db.setdefault('tags', []).append({'id': new_id, 'name': tag_name.strip()})
        return True
    
    def remove_tag(self, tag_name):
        if not tag_name.strip(): return False
        tags = self.db.get('tags', [])
        removed_count = 0
        for i in range(len(tags) - 1, -1, -1):
            if tags[i]['name'].strip().lower() == tag_name.strip().lower():
                del tags[i]
                removed_count += 1
        return bool(removed_count)
    
    def get_tags(self):
        return self.db.get('tags', [])
