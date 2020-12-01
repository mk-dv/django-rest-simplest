from django.db import models


class Author(models.Model):
    """
    An `Article` author

    Attributes:
        name (CharField):
            Author name.
        email (EmailField):
            Author email.
    """

    name = models.CharField(max_length=255)
    email = models.EmailField()


class Article(models.Model):
    """
    Article.

    Attributes:
        title (CharField):
            An article title.
        description (TextField):
            An article description.
        author (ForeignKey[`author`]):
            Article author - instance of `Author` model.
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(
        'Author',
        related_name='articles',
        on_delete=models.CASCADE
    )
