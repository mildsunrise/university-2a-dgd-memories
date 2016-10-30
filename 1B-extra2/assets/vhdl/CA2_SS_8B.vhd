library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_signed.all;

entity CA2_SS_8B is
  port ( x : in std_logic_vector(7 downto 0);
         hex0, hex1, hex2 : out std_logic_vector(6 downto 0));
end;

architecture logic of CA2_SS_8B is
  component CA2_BCD_8B is
  port ( CA2 : in std_logic_vector(7 downto 0);
         BCD : out std_logic_vector(7 downto 0));
  end component;
  component CA2_SIG_SS is
  port ( sig : in std_logic;
         ss : out std_logic_vector(6 downto 0));
  end component;
  component BCD7seg is
  port( num : in std_logic_vector (3 downto 0);
        HEX  : out std_logic_vector (6 downto 0) );
  end component;
  
  signal bcd : std_logic_vector(7 downto 0);
  signal sig, d1, d0 : std_logic_vector(6 downto 0);
begin  
  BCD_M: CA2_BCD_8B port map(CA2 => x, BCD => bcd);
  
  SIG_C: CA2_SIG_SS port map(sig => x(7), ss => sig);
  D1_C: BCD7seg port map(num => bcd(7 downto 4), HEX => d1);
  D0_C: BCD7seg port map(num => bcd(3 downto 0), HEX => d0);
  
  hex0 <= sig when (x <= -10 or x >= +10) else "1111111";
  hex1 <= d1 when (x <= -10 or x >= +10) else sig;
  hex2 <= d0;
end logic;
