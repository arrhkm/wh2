from django.db import models

# Create your models here.

class ItemAttributes(models.Model):
	attr_name = models.CharField(max_length=45, verbose_name="Item Measurement Attributes")

	def __str__(self):
		return str(self.attr_name) 
	
class ItemCategory(models.Model):
	item_category_name = models.CharField(max_length=45, verbose_name="Category Name")

	def __str__(self):
		return self.item_category_name

class ItemRegister(models.Model):
	code_reg = models.CharField(max_length=45, verbose_name="Code")
	name_reg = models.CharField(max_length=45, verbose_name="Register Name")

	def __str__(self):
		return self.code_reg

class Item(models.Model):
	code = models.CharField(max_length=20, primary_key=True)
	item_name = models.CharField(verbose_name="Item Name", max_length=255)
	item_qty = models.DecimalField(verbose_name="Quantity Stock", max_digits=12, decimal_places=2, null=True, blank= True)
	item_register = models.ForeignKey(ItemRegister, null=True, blank=True, default = None, verbose_name="SAP Registered")
	item_category = models.ForeignKey(ItemCategory, null=True, blank=True, default = None, verbose_name="Category")
	item_attribute = models.ForeignKey(ItemAttributes, null=True, blank=True, default = None, verbose_name="ItemAttributes")

	def __str__(self):
		return self.item_name
	
class Bin(models.Model):
	name_location = models.CharField(max_length=45)

	def __str__(self):
		return self.name_location

class SalesOrder(models.Model):
	so_number = models.PositiveIntegerField(primary_key=True)
	so_name = models.CharField(max_length=45)
	so_dscription = models.CharField(max_length=225)

	def __str__(self):
		return str(self.so_number)
	
class SalesOrderPhase(models.Model):	
	phase_number = models.PositiveIntegerField()
	phase_name = models.CharField(max_length=45)
	phase_dscription = models.CharField(max_length=225)
	sales_order = models.ForeignKey(SalesOrder)

	def __str__(self):
		return str(self.sales_order.so_number) + "-" + str(self.phase_number)

class PurchaseOrder(models.Model):
	po_number = models.PositiveIntegerField(primary_key=True)
	supplier_name = models.CharField(max_length=45, null=True, blank=True)	

	def __str__(self):
		return str(self.po_number)

class GrPo(models.Model):
	po_number = models.ForeignKey(PurchaseOrder, verbose_name="Purchase Order", db_column="po_number")
	item_code = models.ForeignKey(Item, verbose_name="Item", related_name='good_received_po', db_column="item_code")
	sales_order_phase_id = models.ForeignKey(SalesOrderPhase, verbose_name="Sales Order", db_column="sales_order_phase_id")
	bin_id = models.ForeignKey(Bin, verbose_name="Bin", null=True, blank=True)
	date_create = models.DateField(verbose_name="Date Created", auto_now_add=True)
	grpo_qty = models.DecimalField(verbose_name="Quantity", max_digits=12, decimal_places=2)

	class Meta:
		unique_together = ('po_number', 'item_code', 'sales_order_phase_id')
		verbose_name = 'Good Received with PO'
		verbose_name_plural = 'Good Received with PO'

	def __str__(self):
		return str(self.po_number) +" - "+ str(self.item_code.code) +" - "+ str(self.item_code.item_name)

	def get_item_code(self):
		return self.item_code.code + " - "+ self.item_code.item_name

	get_item_code.short_description = "Item Code"	

	
	

class GoodIssuedType(models.Model):
	good_issued_name = models.CharField(max_length=45)

	def __str__(self):
		return str(self.good_issued_name)

class GiPo(models.Model):
	issued_number = models.PositiveIntegerField(primary_key=True)
	#good_issued_type_id = models.ForeignKey(GoodIssuedType)
	grpo_id = models.ForeignKey(GrPo, related_name='good_issued_po', db_column='grpo_id')

	date_create = models.DateField(auto_now_add=False)
	dscription = models.CharField(max_length=225)
	qty_issued = models.PositiveIntegerField(max_digits=11)
	received_by = models.CharField(max_length=45)
	sent_location = models.CharField(max_length=45)
	#issued_status = models.PositiveIntegerField(max_digits=1, default=0)
		

	def __str__(self):
		return str(self.issued_number)

	#def save(self, *args, **kwargs):
	#	super(GoodIssued, self).save(*args, **kwargs)
	#	self.grpo.item_code.update_stock()

class issuedPoValue(models.Model):
	gipo_id = models.ForeignKey(GiPo, db_column='gipo_id')
	goodissuedtype_id = models.ForeignKey(GoodIssuedType, db_column='goodissuedtype_id')
	sales_order_phase_id = models.ForeignKey(SalesOrderPhase, db_column='sales_order_phase_id')
	loan_status = models.PositiveIntegerField(max_digits=1, default=0, null=True, blank=True)

	def __str__(self):
		return str(self.goodissuedtype_id.GoodIssuedType.good_issued_name)

class GrNoPo(models.Model):
	bin_id = models.ForeignKey(Bin, null=True, blank=True)
	item_id = models.ForeignKey(Item)
	sales_order_phase_id = models.ForeignKey(SalesOrderPhase)
	date_create = models.DateField(auto_now_add=True)
	po_number = models.PositiveIntegerField(max_digits=11)
	grnopo_qty = models.PositiveIntegerField(max_digits=11)	
	po_status = models.PositiveIntegerField(max_digits=1, null=True, blank=True)
	loan_status = models.PositiveIntegerField(max_digits=1, null=True, blank=True)

	def __str__(self):
		return str(self.sales_order_phase_id)+ "-" + str(self.item_id.code)

class GiNoPo(models.Model):
	grnopo_id = models.ForeignKey(GoodReceiveNoPo, db_column='grnopo_id')
	date_create	= models.DateField(auto_now_add=True)
	ginopo_qty	= models.PositiveIntegerField(max_digits=12, decimal_places=2)
	dscription = models.CharField(max_length=225)
	received_by	= models.CharField(max_length=45)
	sent_location = models.CharField(max_length=45)
	status = models.PositiveIntegerField()	
	
	def __str__(self):
		return str(self.id)

class IssuedNoPoValue(models.Model):
	sales_order_phase_id = models.ForeignKey(SalesOrderPhase)
	ginopo_id = models.ForeignKey(GiNoPo)
	good_issued_type_id = models.ForeignKey(GoodIssuedType)
	posted_status = PositiveIntegerField(max_digits=1, null=True, blank=True)
	class Meta:
		unique_together = ('sales_order_phase_id', 'ginopo_id', 'good_issued_type_id')


class Adjustment(models.Model):
	item_id = models.ForeignKey(Item)
	bin_id = models.ForeignKey(Bin, null=True, blank=True)
	date_created = models.DateField(auto_now_add=True)
	dscription = models.CharField(max_length=225, null=True, blank=True)
	adjustment_qty = models.PositiveIntegerField()
	adjustment_actived = models.PositiveIntegerField(max_digits=1, default=1)



class IssuedAdjusment(models.Model):
	adjustment_id = models.ForeignKey(Adjustment)
	sales_order_phase_id = models.ForeignKey(SalesOrderPhase)
	issued_date = models.DateField(auto_now_add=True)
	issued_qty = PositiveIntegerField()