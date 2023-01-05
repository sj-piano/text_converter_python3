# Imports
import pytest
import pkgutil




# Relative imports
from .. import code
from .. import util
from .. import submodules




# Shortcuts
utf8_latin_1_to_eml = code.convert.utf8_latin_1_to_eml




# Setup for this file.
@pytest.fixture(autouse=True, scope='module')
def setup_module(pytestconfig):
  # If log_level is supplied to pytest in the commandline args, then use it to set up the logging in the application code.
  log_level = pytestconfig.getoption('log_cli_level')
  if log_level is not None:
    log_level = log_level.lower()
    code.setup(log_level = log_level)
    submodules.setup(log_level = log_level)








# ### SECTION
# Basic checks.




def test_1():
  x = "La difficulté de réussir ne fait qu'ajouter à la nécessité d'entreprendre."
  y = "L_a_  d_i_f_f_i_c_u_l_t_e'  d_e_  r_e'u_s_s_i_r_  n_e_  f_a_i_t_  q_u_'_a_j_o_u_t_e_r_  a`  l_a_  n_e'c_e_s_s_i_t_e'  d_'_e_n_t_r_e_p_r_e_n_d_r_e_._"
  assert utf8_latin_1_to_eml(x) == y


def test_2():
  x = "Qui craint de souffrir, il souffre déjà de ce qu'il craint."
  y = "Q_u_i_  c_r_a_i_n_t_  d_e_  s_o_u_f_f_r_i_r_,_  i_l_  s_o_u_f_f_r_e_  d_e'j_a`  d_e_  c_e_  q_u_'_i_l_  c_r_a_i_n_t_._"
  assert utf8_latin_1_to_eml(x) == y



