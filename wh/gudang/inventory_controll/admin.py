from django.contrib import admin

# Register your models here.
from inventory_controll.models import ItemAttributes, ItemCategory, ItemRegister, Item,  SalesOrder, Bin,\
									  SalesOrderPhase, PurchaseOrder, GrPo, GoodIssuedType,  GiPo,\
									  Adjustment, IssuedAdjustment 
class ItemAdmin(admin.ModelAdmin):
	list_display = ['code', 'item_name', 'item_qty', 'item_register', 'item_category', 'item_attribute']
	list_filter = ('item_category__item_category_name',)
	#fields = (('code', 'item_name'), 'item_register', 'item_category', 'item_attribute')
	fieldsets = (
		('Item Information', {
			'fields': (('code', 'item_name'), 'item_register', 'item_category', 'item_attribute')
		}),
	)
	search_fields = ['code', 'item_name']

	def get_readonly_fields(self, request, obj=None):
		readonly_fields = []
		if obj is not None:
			readonly_fields.append('code')
		return readonly_fields

class ItemAttributesAdmin(admin.ModelAdmin):
	list_display = ['id', 'attr_name']

class ItemCategoryAdmin(admin.ModelAdmin):
	pass

class ItemRegisterAdmin(admin.ModelAdmin):
	list_display = ['code_reg', 'name_reg']

class SalesOrderPhaseInline(admin.TabularInline):
	model = SalesOrderPhase
	extra = 2
	list_filter = ('sales_order',)

class SalesOrderAdmin(admin.ModelAdmin):
	list_display = ('so_number', 'so_name', 'so_dscription')
	inlines = [SalesOrderPhaseInline,]

@admin.register(SalesOrderPhase)
class SalesOrderPhaseAdmin(admin.ModelAdmin):
	list_display = ('sales_order', '_phase_number', 'phase_name', 'phase_dscription', 'get_total_in_grpo')
	list_filter = ('sales_order',)

class PurchaseOrderAdmin(admin.ModelAdmin):
	list_display = ('po_number', 'supplier_name')

class GrPoAdmin(admin.ModelAdmin):
	list_display = ('sales_order_phase_id', 'po_number', 'item_code', 'date_create', 'grpo_qty', 'bin_id', 'status_po')
	list_filter = ('sales_order_phase_id', 'po_number', 'item_code', 'status_po')

class GoodIssuedTypeAdmin(admin.ModelAdmin):
	pass

class IssuedNoPoValueAdmin(admin.ModelAdmin):
	pass

class GiPoAdmin(admin.ModelAdmin):
	list_display = ('issued_number', 'grpo_id', 'good_issued_type_id', 'sales_order_phase_id', 'so_phase2', 'grpo_id2',  'qty_issued')

class AdjustmentAdmin(admin.ModelAdmin):
	list_display = ('id', 'dscription', 'item_id', 'date_created', 'bin_id', 'adjustment_qty', 'saldo_qty', 'adjustment_actived')

class IssuedAdjustmentAdmin(admin.ModelAdmin):
	list_display = ('adjustment_id', 'sales_order_phase_id', 'issued_date', 'issued_qty')
# Register Class admin 
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemAttributes, ItemAttributesAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(ItemRegister, ItemRegisterAdmin)
admin.site.register(SalesOrder, SalesOrderAdmin)
#admin.site.register(SalesOrderPhase, SalesOrderPhaseAdmin)

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
admin.site.register(Bin)
admin.site.register(GrPo, GrPoAdmin)
admin.site.register(GoodIssuedType, GoodIssuedTypeAdmin)
admin.site.register(GiPo, GiPoAdmin)
admin.site.register(Adjustment, AdjustmentAdmin)
admin.site.register(IssuedAdjustment, IssuedAdjustmentAdmin)

