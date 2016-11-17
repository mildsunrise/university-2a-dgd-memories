library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity AperB is
  port ( A,B : in std_logic_vector(3 downto 0);
         AxB : out std_logic_vector(7 downto 0) );
end;

architecture logic of AperB is
  component CA2_BCD_8B is
    port ( CA2 : in std_logic_vector(7 downto 0);
           BCD : out std_logic_vector(7 downto 0) );
  end component;

  signal res : std_logic_vector(7 downto 0);
begin
  res <= A*B;
  D0: CA2_BCD_8B port map(CA2 => res, BCD => AxB);
end logic;
