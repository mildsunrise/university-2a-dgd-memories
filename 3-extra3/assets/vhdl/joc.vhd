library ieee;
use ieee.std_logic_1164.all;

entity joc is
  port ( clk, nrst : in std_logic;
         nkey : in std_logic;
         keycode : in std_logic_vector(3 downto 0);
         comp : out std_logic_vector(2 downto 0);
         num : out std_logic_vector(11 downto 0) );
end;

architecture components of joc is
  component keygroup is
    port ( x : in std_logic_vector(3 downto 0);
           nkey : in std_logic;
           bcd, ast, coi, let : out std_logic );
  end component;
  
  component control is
    port ( bcd, ast, coi, let : in std_logic;
           ngtx, neqx, nltx : in std_logic;
           clk, nrst : in std_logic;
           eshft, ecnt, show : out std_logic;
           comp : out std_logic_vector(2 downto 0) );
  end component;
  
  component registres is
    port ( clk : in std_logic;
           nrst : in std_logic;
           eshft : in std_logic;
           keycode : in std_logic_vector(3 downto 0);
           num : out std_logic_vector(11 downto 0) );
  end component;
  
  component comptador is
    port ( ecnt : in std_logic;
           nrst, clk : in std_logic;
           numx : out std_logic_vector(11 downto 0) );
  end component;
  
  component comparador is
    port ( numx, num : in std_logic_vector(11 downto 0);
           ngtx, neqx, nltx : out std_logic );
  end component;
  
  signal bcd, ast, coi, let : std_logic;
  signal ecnt, eshft, show : std_logic;
  signal num_i, numx : std_logic_vector(11 downto 0);
  signal ngtx, neqx, nltx : std_logic;
begin

  keygroup_inst : keygroup port map (
    nkey => nkey, x => keycode,
    bcd => bcd, ast => ast, coi => coi, let => let
  );
  
  control_inst : control port map (
    clk => clk, nrst => nrst,
    bcd => bcd, ast => ast, coi => coi, let => let,
    ngtx => ngtx, neqx => neqx, nltx => nltx,
    ecnt => ecnt, eshft => eshft, show => show, comp => comp
  );

  comptador_inst : comptador port map (
    clk => clk, nrst => nrst,
    ecnt => ecnt,
    numx => numx
  );

  registres_inst : registres port map (
    clk => clk, nrst => nrst,
    eshft => eshft, keycode => keycode,
    num => num_i
  );
  
  comparador_inst : comparador port map (
    numx => numx, num => num_i,
    ngtx => ngtx, neqx => neqx, nltx => nltx
  );

  num <= num_i when show = '0' else numx;

end components;
