from ast import AstNodeTypes


class Visitor(object):

    def visit(self, node, jsonKey):
        if jsonKey == AstNodeTypes.DOCUMENT:
            self.visitDocument(node)
        elif jsonKey == AstNodeTypes.OBJECT:
            self.visitObject(node)
        elif jsonKey == AstNodeTypes.ARRAY:
            self.visitArray(node)
        elif jsonKey == AstNodeTypes.BOOLEAN:
            self.visitBoolean(node)
        elif jsonKey == AstNodeTypes.COMMENT:
            self.visitComment(node)
        elif jsonKey == AstNodeTypes.KEY:
            self.visitKey(node)
        elif jsonKey == AstNodeTypes.NUMBER:
            self.visitNumber(node)
        elif jsonKey == AstNodeTypes.PAIR:
            self.visitPair(node)
        elif jsonKey == AstNodeTypes.STRING:
            self.visitString(node)
        elif jsonKey == AstNodeTypes.VALUE:
            self.visitValue(node)

    def visitDocument(self, doc):
        pass

    def visitObject(self, obj):
        pass

    def visitPair(self, pair):
        pass

    def visitKey(self, key):
        pass

    def visitString(self, jsonString):
        pass

    def visitNumber(self, jsonNumber):
        pass

    def visitValue(self, jsonValue):
        pass

    def visitBoolean(self, jsonBoolen):
        pass

    def visitNode(self, jsonNode):
        pass

    def visitComment(self, jsonComment):
        pass

    def visitArray(self, jsonArray):
        pass
