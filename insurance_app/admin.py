
from django.contrib import admin
from .models import InsuranceData

# Optional: Custom action to delete records in bulk
def delete_selected_records(modeladmin, request, queryset):
    queryset.delete()
delete_selected_records.short_description = "Delete selected records"

# Admin configuration for the InsuranceData model
@admin.register(InsuranceData)
class InsuranceAdmin(admin.ModelAdmin):
    # Fields to be displayed in the admin list view
    list_display = ('age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges', 'coverage')
    # Fields to enable filtering by in the sidebar
    list_filter = ('sex', 'smoker', 'region', 'children')
    # Fields to enable searching
    search_fields = ('age', 'bmi', 'charges', 'coverage')
    # Custom actions to be available in the list view
    actions = [delete_selected_records]

    # Customizing the form displayed on the add/edit page
    fieldsets = (
        (None, {
            'fields': ('age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges', 'coverage')
        }),
    )

    # Optionally make certain fields editable directly in the list display
    list_editable = ('bmi', 'charges', 'coverage')


