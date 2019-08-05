# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions

class LibraryBook(models.Model):
    _name = 'library.book'

    name = fields.Char(string='Book', default="Nuevo Libro",)
    description = fields.Text(string='Description')
    isbn = fields.Char(string='ISBN')

    category_id = fields.Many2one(
        comodel_name="library.category", string="Categoría Many2one",
        required=False)

    category_ids = fields.Many2many(
        comodel_name="library.category", string="Categorías Many2many",
        required=False)

    category_idos = fields.One2many(
        comodel_name="library.category",
        inverse_name="book_id",
        string="Categorías One2many",
        required=False)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "El libro ya está agregado!!"),
    ]

    categ_count = fields.Integer(
        string="Nro categorías",
        compute="_count_categ"
    )

    #def _count_categ(self):
    #    self.categ_count = len(self.category_ids)

    def _count_categ(self):
        for book in self:
                book.categ_count = len(book.category_ids)

    @api.constrains("isbn")
    def check_isbn(self):
        isbn = self.search([['id', '!=', self.id]]).mapped("isbn")
        if self.isbn and self.isbn in isbn:
            raise exceptions.ValidationError("ISBN Duplicado")