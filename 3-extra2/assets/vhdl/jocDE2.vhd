library ieee;
use ieee.std_logic_1164.all;

library work;

entity jocDE2 is
  port ( OSC_50 : in std_logic;
         KEY : in std_logic_vector(3 downto 0);
         COL : in std_logic_vector(3 downto 0);
         ROW : out std_logic_vector(3 downto 0);
         HEX7, HEX6, HEX5, HEX4, HEX3, HEX2, HEX1, HEX0 : out std_logic_vector(6 downto 0);
         LED_GREEN : out std_logic_vector(7 downto 0) );
end jocDE2;

architecture bdf_type of jocDE2 is
  component f_div
    port ( nrst : in std_logic;
           clkin : in std_logic;
           clkout : out std_logic );
  end component;
  
  component keytest
    port( clk : in std_logic;
          nrst : in std_logic;
          col : in std_logic_vector(3 downto 0);
          nkey : out std_logic;
          keycode : out std_logic_vector(3 downto 0);
          row : out std_logic_vector(3 downto 0) );
  end component;
  
  component joc
    port ( nkey : in std_logic;
           clk : in std_logic;
           nrst : in std_logic;
           keycode : in std_logic_vector(3 downto 0);
           comp : out std_logic_vector(2 downto 0);
           num : out std_logic_vector(11 downto 0) );
  end component;
  
  component leds
    port ( comp : in std_logic_vector(2 downto 0);
           led_green : out std_logic_vector(7 downto 0) );
  end component;
  
  component hex_disps
    port ( num7, num6, num5, num4, num3, num2, num1, num0 : in std_logic_vector(3 downto 0);
           HEX0 : out std_logic_vector(6 downto 0);
           HEX1 : out std_logic_vector(6 downto 0);
           HEX2 : out std_logic_vector(6 downto 0);
           HEX3 : out std_logic_vector(6 downto 0);
           HEX4 : out std_logic_vector(6 downto 0);
           HEX5 : out std_logic_vector(6 downto 0);
           HEX6 : out std_logic_vector(6 downto 0);
           HEX7 : out std_logic_vector(6 downto 0) );
  end component;

  signal clk, nrst : std_logic;
  signal nkey : std_logic;
  signal keycode : std_logic_vector(3 downto 0);
  signal comp : std_logic_vector(2 downto 0);
  signal num : std_logic_vector(11 downto 0);
  
  signal blank : std_logic_vector(3 downto 0);
begin

  -- Generació del clock i reset

  nrst <= KEY(0);

  clk_div : f_div port map(
    nrst => nrst,
    clkin => OSC_50,
    clkout => clk
  );

  -- Escaneig del teclat

  keytest_inst : keytest port map(
    clk => clk, nrst => nrst,
    col => COL, row => ROW,
    nkey => nkey, keycode => keycode
  );

  -- El joc en sí

  joc_inst : joc port map(
    clk => clk, nrst => nrst,
    nkey => nkey, keycode => keycode,
    comp => comp, num => num
  );

  -- LEDs, displays

  leds_inst : leds port map(
    comp => comp,
    led_green => LED_GREEN
  );

  blank <= "1111";

  hex_disps_inst : hex_disps port map(
    num7 => blank,
    num6 => blank,
    
    num5 => blank,
    num4 => blank,
    
    num3 => blank,
    num2 => num(11 downto 8),
    num1 => num(7 downto 4),
    num0 => num(3 downto 0),
    
    HEX7 => HEX7, HEX6 => HEX6, HEX5 => HEX5, HEX4 => HEX4,
    HEX3 => HEX3, HEX2 => HEX2, HEX1 => HEX1, HEX0 => HEX0
  );

end bdf_type;
