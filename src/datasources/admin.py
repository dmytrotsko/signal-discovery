from typing import Literal

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from datasources.models import DataSource, SourceSubdivision
from datasources.resources import SourceSubdivisionResource


@admin.register(SourceSubdivision)
class SourceSubdivisionAdmin(ImportExportModelAdmin):
    """
    Admin interface for managing source subdivision objects.
    """
    list_display: tuple[Literal['name'], Literal['display_name'], Literal['data_source']] = (
        'name', 'display_name', 'data_source')
    search_fields: tuple[Literal['name'], Literal['db_source']] = ('name', 'db_source')
    resource_classes: list[type[SourceSubdivisionResource]] = [SourceSubdivisionResource]


@admin.register(DataSource)
class DataSourceAdmin(ImportExportModelAdmin):
    """
    Admin interface for managing data source objects.
    """
    list_display: tuple[Literal['name']] = ('name',)
    search_fields: tuple[
        Literal['name'], Literal['source_subdivision__name'], Literal['description']]
    search_fields = ('name', 'source_subdivision__name', 'description')
