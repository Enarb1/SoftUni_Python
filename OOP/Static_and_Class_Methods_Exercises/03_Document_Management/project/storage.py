from typing import List
from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def get_document(self, document_id: int):
        return next(filter(lambda d: d.id == document_id, self.documents))

    def get_topic(self, topic_id:int):
        return next(filter(lambda t: t.id == topic_id, self.topics))

    def get_category(self, category_id: int):
        return next(filter(lambda c: c.id == category_id, self.categories))

    def edit_category(self, category_id: int, new_name: str) -> None:
        category = self.get_category(category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        topic = self.get_topic(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        document = self.get_document(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id: int) -> None:
        category = self.get_category(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id: int) -> None:
        topic = self.get_topic(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id: int) -> None:
        document = self.get_document(document_id)
        self.documents.remove(document)

    def __repr__(self):
        return "\n".join(str(d) for d in self.documents)

