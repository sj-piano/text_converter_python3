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
  x = "(si lo fuera realmente ¿a qué esa duplicación ilusoria?);"
  y = "(_s_i_  l_o_  f_u_e_r_a_  r_e_a_l_m_e_n_t_e_  ?ia_  q_u_e'  e_s_a_  d_u_p_l_i_c_a_c_i_o'n_  i_l_u_s_o_r_i_a_?_)_;_"
  assert utf8_latin_1_to_eml(x) == y


def test_2():
  x = "galerías hexagonales,"
  y = "g_a_l_e_r_i'a_s_  h_e_x_a_g_o_n_a_l_e_s_,_"
  assert utf8_latin_1_to_eml(x) == y


def test_tabs():
  x = "\t\t"
  y = "-\t-\t"
  x = "\t\tLa luz procede de unas frutas esféricas"
  y = "-\t-\tL_a_  l_u_z_  p_r_o_c_e_d_e_  d_e_  u_n_a_s_  f_r_u_t_a_s_  e_s_f_e'r_i_c_a_s_"
  assert utf8_latin_1_to_eml(x) == y


def test_newline():
  x = """
yo prefiero soñar que las superficies bruñidas figuran y prometen el infinito...
La luz procede de unas frutas esféricas
""".strip()
  y = """
y_o_  p_r_e_f_i_e_r_o_  s_o_n~a_r_  q_u_e_  l_a_s_  s_u_p_e_r_f_i_c_i_e_s_  b_r_u_n~i_d_a_s_  f_i_g_u_r_a_n_  y_  p_r_o_m_e_t_e_n_  e_l_  i_n_f_i_n_i_t_o_._._._+
L_a_  l_u_z_  p_r_o_c_e_d_e_  d_e_  u_n_a_s_  f_r_u_t_a_s_  e_s_f_e'r_i_c_a_s_
""".strip()
  assert utf8_latin_1_to_eml(x) == y



