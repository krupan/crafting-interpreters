#!/usr/bin/env python3
from dataclasses import dataclass, field

from token_type import Token, TokenType


@dataclass
class Scanner:
    source: str
    # essentially private class members:
    tokens: list[Token] = field(default_factory=list, init=False)
    start: int = field(default=0, init=False, repr=False)
    current: int = field(default=0, init=False, repr=False)
    line: int = field(default=1, init=False, repr=False)

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()
        match c:
            case '(': self.add_token(TokenType.LEFT_PAREN)
            case ')': self.add_token(TokenType.RIGHT_PAREN)
            case '{': self.add_token(TokenType.LEFT_BRACE)
            case '}': self.add_token(TokenType.RIGHT_BRACE)
            case ',': self.add_token(TokenType.COMMA)
            case '.': self.add_token(TokenType.DOT)
            case '-': self.add_token(TokenType.MINUS)
            case '+': self.add_token(TokenType.PLUS)
            case ';': self.add_token(TokenType.SEMICOLON)
            case '*': self.add_token(TokenType.STAR)

    def advance(self):
        self.current += 1
        return self.source[self.current]

    def add_token(self, token, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(token, text, literal, self.line))

    def is_at_end(self):
        return self.current >= len(self.source)
