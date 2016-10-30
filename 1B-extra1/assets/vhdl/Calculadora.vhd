library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_signed.all;

entity Calculadora is
  port ( A,B : in std_logic_vector(3 downto 0);
         selop : in std_logic_vector(1 downto 0);
         Z : out std_logic_vector(7 downto 0);
         r : out std_logic);
end;

architecture logic of Calculadora is
  component DEC_3B is
  port ( a : in std_logic_vector(2 downto 0);
         z : out std_logic_vector(7 downto 0));
  end component;
  
  signal S : std_logic_vector(3 downto 0);
  signal s_in_range : boolean;
  signal P : std_logic_vector(7 downto 0);
begin  
  S <= A+B;
  s_in_range <= A(3) /= B(3) or A(3) = S(3);
  dec1: DEC_3B port map(a => S(2 downto 0), z => P);
  
  with selop select
    Z <= A*B when "00",
         A*A when "01",
         B*B when "10",
         P   when others;
  
  r <= '0' when (s_in_range and S >= 0 and S <= 6) or selop /= "11" else '1';
end logic;
