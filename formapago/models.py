from django.template.defaultfilters import slugify
from django.db import models
from django.urls import reverse
from django.utils import timezone


class i001t_tipo_forma_pago(models.Model):
    """
    Modelo que representa tipo de Forma de Pago. """
    co_tipo_forma_pago       = models.AutoField(primary_key=True,verbose_name='codigo')
    tx_nombre                = models.CharField(max_length=50, verbose_name='nombre', help_text="Ingrese nombre de la oficina")
    tx_enlace                = models.SlugField(max_length=110,unique=True,null=False,verbose_name='enlace',help_text='Unique value for product page URL, created from name.')
    nu_orden                 = models.IntegerField(blank=True, null=True,default='1',verbose_name='Orden',help_text='Orden de presentacion de tienda en destacados')
    fe_crea                  = models.DateTimeField(default=timezone.now,verbose_name='fecha crea', help_text="Seleccione fecha de creación del registro")
    fe_modifica              = models.DateTimeField(default=timezone.now,verbose_name='fecha modifica', help_text="Seleccione fecha de modificación del registro")
    tx_observacion           = models.CharField(max_length=50,null=True,default='Forma de Pago', help_text="Ingrese observacion relevante del registro")
    in_activo                = models.BooleanField(default=True,verbose_name='activo')

    class Meta:
        ordering = ["-fe_crea"]
        verbose_name        = "Tipo Forma de Pago"
        verbose_name_plural = "Tipo Formas de Pago"
        db_table = "i001t_tipo_forma_pago"

    def __str__(self):
        return self.tx_nombre

    def save(self, *args, **kwargs):
        self.tx_enlace = slugify(self.tx_nombre)
        super(i001t_tipo_forma_pago, self).save(*args, **kwargs)

class i002t_forma_pago(models.Model):
    """
    Modelo que representa de Forma de Pago. """
    co_forma_pago              = models.AutoField(primary_key=True,verbose_name='codigo')
    co_tipo                    = models.ForeignKey(i001t_tipo_forma_pago,on_delete=models.PROTECT,verbose_name='Tipo',related_name='co_tipo_forma_pago_forma_pago', help_text="Seleccione Tipo")
    #co_farmacia                = models.ForeignKey(i001t_minifarmacia,on_delete=models.PROTECT,null=False,blank=False,verbose_name='Farmacia',related_name='co_farmacia_forma_pago', help_text="Seleccione Farmacia")
    tx_nombre                  = models.CharField(max_length=50,unique=True,null=False, verbose_name='nombre',default='Forma de Pago', help_text="Ingrese nombre de la forma de pago")
    tx_enlace                  = models.SlugField(max_length=110,unique=True,null=False,verbose_name='enlace',help_text='URL de la página de la forma de pago, creado a partir del nombre.')
    nu_orden                   = models.IntegerField(blank=True, null=True,default='1',verbose_name='Orden',help_text='Orden de presentacion de la forma de pago segun su uso')
    tx_nombre_titular          = models.CharField(max_length=50,null=True,default='Elvis Gamboa',verbose_name='Nombre', help_text="Ingrese Nombre del titular de la cuenta bancaria")
    tx_cedula_titular          = models.CharField(max_length=50,null=True,default='15908576',verbose_name='Cedula', help_text="Ingrese Cedula del titular de la cuenta bancaria")
    tx_correo_titular          = models.CharField(max_length=50,null=True,default='gamboaej@hotmail.com',verbose_name='Correo Electrónico', help_text="Ingrese Correo del titular de la cuenta bancaria")
    tx_telefono_titular        = models.CharField(max_length=50,null=True,default='0000-0000000',verbose_name='Telefono', help_text="Ingrese Numero de telefono del titular de la cuenta bancaria")
    tx_numero_cuenta           = models.CharField(max_length=50,null=True,default='0000-0000-0000-0000-0000',verbose_name='Numero Cuenta',help_text="Ingrese Numero de la cuenta bancaria")
    tx_tipo_cuenta             = models.CharField(max_length=50,null=True,default='AAAAAAA',verbose_name='Tipo de Cuenta', help_text="Ingrese Tipo de Cuenta bancaria")
    tx_codigo_banco            = models.CharField(max_length=50,null=True,default='0000', verbose_name='Codigo de Banco', help_text="Ingrese Codigo del Banco de la cuenta bancaria")
    tx_direccion_cartera       = models.CharField(max_length=50,null=True,default='D5pb932C7ugcMkbCpgw4hQDDzB5wgKd2eg',verbose_name='Direccion Cartera', help_text="Ingrese Cartera de criptomoneda")
    tx_foto                    = models.ImageField(upload_to='formapago',default='formapago/fp_no_disponible.png',verbose_name='imagen')
    fe_crea                    = models.DateTimeField(default=timezone.now,verbose_name='fecha crea', help_text="Seleccione fecha de creación del registro")
    fe_modifica                = models.DateTimeField(default=timezone.now,verbose_name='fecha modifica', help_text="Seleccione fecha de modificación del registro")
    tx_observacion             = models.CharField(max_length=50,null=True,default='Forma de Pago', verbose_name='Observacion', help_text="Ingrese observacion relevante del registro")
    in_activo                  = models.BooleanField(default=True,verbose_name='activo')

    class Meta:
        ordering = ["-fe_crea"]
        verbose_name        = "Forma de Pago"
        verbose_name_plural = "Formas de Pago"
        db_table = "i002t_forma_pago"

    def __str__(self):
        return self.tx_nombre

    def save(self, *args, **kwargs):
        self.tx_enlace = slugify(self.tx_nombre)
        super(i002t_forma_pago, self).save(*args, **kwargs)
