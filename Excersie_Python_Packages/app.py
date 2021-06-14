import ecommerce.shipping # import Module ecommerce(package/folder) and continues with the following import to shipping(module/file)
from ecommerce.shipping import calc_shipping # import function
from ecommerce import  shipping


ecommerce.shipping.calc_shipping()  #way to IMPORT  1


calc_shipping()                     #way to IMPORT  2


shipping.calc_shipping()            #way to IMPORT  3