from django.db import models
from django.db.models import Sum

#Create Custom Manager Query set


# Create your models here.

class ItemAttributes(models.Model):
	attr_name = models.CharField(max_length=45, verbose_name="Item Measurement Attributes")

	class Meta:
		verbose_name = 'ITEM ATTRIBUTE'
		verbose_name_plural = 'ITEM ATTRIBUTE'

	def __str__(self):
		return str(self.attr_name) 
	
class ItemCategory(models.Model):
	item_category_name = models.CharField(max_length=45, verbose_name="Category Name")

	class Meta:
		verbose_name = 'ITEM CATTEGORY'
		verbose_name_plural = 'ITEM CATTEGORIES'

	def __str__(self):
		return self.item_category_name

class ItemRegister(models.Model):
	code_reg = models.CharField(max_length=45, verbose_name="Code")
	name_reg = models.CharField(max_length=45, verbose_name="Register Name")

	class Meta:
		verbose_name = 'ITEM REGISTER'
		verbose_name_plural = 'ITEM REGISTRERS'

	def __str__(self):
		return self.code_reg

class Item(models.Model):
	code = models.CharField(max_length=20, primary_key=True, verbose_name="Code")
	item_name = models.CharField(verbose_name="Name", max_length=255)
	item_qty = models.PositiveIntegerField(null=True, blank= True, default=0)
	item_register = models.ForeignKey(ItemRegister, null=True, blank=True, default = None, verbose_name="Register")
	item_category = models.ForeignKey(ItemCategory, null=True, blank=True, default = None, verbose_name="Category")
	item_attribute = models.ForeignKey(ItemAttributes, null=True, blank=True, default = None, verbose_name="Attributes")

	class Meta:
		verbose_name = 'ITEM'
		verbose_name_plural = 'ITEM'

	def __str__(self):
		return self.item_name

class Bin(models.Model):
	name_location = models.CharField(max_length=45, verbose_name="Location Name")

	def __str__(self):
		return self.name_location
	class Meta:
		verbose_name_plural = 'BIN'
		verbose_name_plural = 'BIN'

class SalesOrder(models.Model):
	so_number = models.PositiveIntegerField(primary_key=True, verbose_name="Number")
	so_name = models.CharField(max_length=45, verbose_name="Name")
	so_dscription = models.CharField(max_length=225, verbose_name="Description")

	class Meta:
		verbose_name = 'SALES ORDER'
		verbose_name_plural = 'SALES ORDERS'

	def __str__(self):
		return str(self.so_number)

class SalesOrderPhase(models.Model):
	phase_number = models.PositiveIntegerField(verbose_name="Phase Number")
	phase_name = models.CharField(max_length=45, null=True, blank=True, verbose_name="Name")
	phase_dscription = models.CharField(max_length=225, null=True, blank=True, verbose_name="Description")
	sales_order = models.ForeignKey(SalesOrder, verbose_name="Sales Order")

	class Meta:
		verbose_name = 'SO PHASE'
		verbose_name_plural = 'SO PHASE'

	def __str__(self):
		return str(self.sales_order.so_number) + "-" + str(self.phase_number).zfill(3)

	def _phase_number(self):
		return str(self.phase_number).zfill(3)
	_phase_number.short_description = 'Phase Number'

	def get_total_in_grpo(self):
		# return self.grpo_set.filter(sales_order_phase_id=self.id).aggregate(Sum('grpo_qty'))['grpo_qty__sum']
		pass


class PurchaseOrder(models.Model):
	po_number = models.CharField(max_length=20,primary_key=True, verbose_name="Number")
	supplier_name = models.CharField(max_length=45, null=True, blank=True, verbose_name="Supplier")

	class Meta:
		verbose_name = 'PURCHASE ORDER'
		verbose_name_plural = 'PURCHASE ORDER LIST'

	def __str__(self):
		return str(self.po_number)


class SOPhaseSummary(models.Manager):
	def get_queryset(self):
		return super(SOPhaseSummary, self).get_queryset().select_related('sales_order_phase_id').values(
			'item_code__item_name',
			'sales_order_phase_id__phase_number',
			'sales_order_phase_id__sales_order'
		).annotate(total=Sum('grpo_qty'))

class SOSummary(models.Manager):
	def get_queryset(self):
		return super(SOSummary, self).get_queryset().select_related('sales_order_phase_id').values(
			'item_code__item_name',
			'sales_order_phase_id__sales_order'
		).annotate(total=Sum('grpo_qty'))

class GrPo(models.Model):
	po_number = models.ForeignKey(PurchaseOrder, verbose_name="Purchase Order", db_column="po_number")
	item_code = models.ForeignKey(Item, verbose_name="Item", related_name='good_received_po', db_column="item_code")
	sales_order_phase_id = models.ForeignKey(SalesOrderPhase, verbose_name="Sales Order", db_column="sales_order_phase_id")
	bin_id = models.ForeignKey(Bin, verbose_name="Bin", null=True, blank=True)
	date_create = models.DateField(verbose_name="Date Created", auto_now_add=True)
	grpo_qty = models.PositiveIntegerField(verbose_name="Quantity")
	status_po = models.BooleanField()
	saldo_qty = models.PositiveIntegerField(null=True, blank=True)

	class Meta:
		unique_together = ('po_number', 'item_code', 'sales_order_phase_id')
		verbose_name = 'GRPO'
		verbose_name_plural = 'GRPO'

	objects = models.Manager()
	summary_by_so_phase = SOPhaseSummary()
        summary_by_so = SOSummary()

	def __str__(self):
		return str(self.po_number) +" - "+ str(self.item_code.code) +" - "+ str(self.item_code.item_name)

	def get_item_code(self):
		return self.item_code.code + " - "+ self.item_code.item_name

	get_item_code.short_description = "Item Code"

	def get_total_item(self):
		obj = self.objects.aggregate(Sum('grpo_qty'))['grpo_qty_sum']
		return obj

	get_total_item.short_description = "Quantity"

class GoodIssuedType(models.Model):
	good_issued_name = models.CharField(max_length=45, verbose_name="Good Issued Name")

	def __str__(self):
		return str(self.good_issued_name)
	class Meta:
		verbose_name = "GOOD ISSUED TYPE"
		verbose_name_plural = "GOOD ISSUED LIST"


class GiPo(models.Model):
	issued_number = models.CharField(max_length=20, primary_key=True, verbose_name="Issued Number")
	good_issued_type_id = models.ForeignKey(GoodIssuedType, verbose_name="Good Issued Type")
	grpo_id = models.ForeignKey(GrPo, related_name='good_issued_po', db_column='grpo_id')
	sales_order_phase_id = models.ForeignKey(SalesOrderPhase, db_column='sales_order_phase_id', null=True, blank=True)
	so_phase2 = models.ForeignKey(SalesOrderPhase, related_name='so_phase_issued2', db_column='so_phase2', null=True, blank=True)
	grpo_id2 = models.ForeignKey(GrPo, related_name='gr_po_issued2', db_column='grpo_id2', null=True, blank=True)
	qty_issued = models.PositiveIntegerField(verbose_name="Quantity")	
	date_create = models.DateField(auto_now_add=False, verbose_name="Date Created")
	dscription = models.CharField(max_length=225, null=True, blank=True, verbose_name="Description")	
	received_by = models.CharField(max_length=45, null=True, blank=True, verbose_name="Received by")
	sent_location = models.CharField(max_length=45, null=True, blank=True, verbose_name="Sent Location")
	status_rent = models.BooleanField(default=False)

	class Meta:
		verbose_name = "GIPO"
		verbose_name_plural = 'GIPO'

	def __str__(self):
		return str(self.issued_number)

class Adjustment(models.Model):
	CHOICES = ((1, 'ACTIVE'), (0, 'CLOSED'))
	item_id = models.ForeignKey(Item, verbose_name="Item")
	bin_id = models.ForeignKey(Bin, null=True, blank=True, verbose_name="Bin")
	date_created = models.DateField(auto_now_add=True, verbose_name="Date Created")
	dscription = models.CharField(max_length=225, null=True, blank=True, verbose_name="Description")
	adjustment_qty = models.PositiveIntegerField(verbose_name="Quantity", blank=True, null=False, default=0)
	saldo_qty = models.PositiveIntegerField(blank=True, null=False, default=0)
	adjustment_actived = models.PositiveIntegerField(default=1, choices=CHOICES, verbose_name="Status")

	class Meta:
		verbose_name = "ADJUSTMENT"
		verbose_name_plural = "ADJUSTMENT"
	def __str__(self):
		return str(self.dscription)+ " - " + str(self.item_id.item_name)

class IssuedAdjustment(models.Model):
	adjustment_id = models.ForeignKey(Adjustment, verbose_name="Adjustment")
	sales_order_phase_id = models.ForeignKey(SalesOrderPhase, verbose_name="Sales Order Phase")
	issued_date = models.DateField(auto_now_add=True, verbose_name="Issued Date")
	issued_qty = models.PositiveIntegerField(verbose_name="Quantity", blank=True, null=False, default=1)

	class Meta:
		verbose_name = "ISSUED ADJUSTMENT"
		verbose_name_plural = "ISSUED ADJUSTMENT"

	def __str__(self):
		return str(self.adjustment_id)
