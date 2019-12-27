# a package is a file for multiple items.
# packages need to have a file called __init__ in it
# multiple ways to call a package

import ecommerce.shipping  # whole module
ecommerce.shipping.calc_shipping()

from ecommerce.shipping import calc_shipping  # import function from specific module

calc_shipping()

from ecommerce import shipping  # specific module

shipping.calc_shipping()
