CREATE TABLE Livros (
Titulo VARCHAR(50) NOT NULL,
Autor VARCHAR (50) NOT NULL,
CodigoID INT NOT NULL,
Genero VARCHAR (50),
PRIMARY KEY (CodigoID));

CREATE TABLE Emprestimos (
CpfID VARCHAR(11) NOT NULL,
CodigoID INT NOT NULL,
Nome_Cliente VARCHAR (50),
Data_Emprestimo DATE NOT NULL,
PRIMARY KEY (CpfID),
FOREIGN KEY  (CodigoID) REFERENCES Livros(CodigoID)
);

INSERT INTO Livros  (Titulo, Autor, CodigoID, Genero)
VALUES ('O Acordo', 'Elle', 121212, 'Romance'),
('O Erro', 'Elle', 131313, 'Romance'),
('O Jogo', 'Elle', 141414, 'Romance'),
('A Conquista', 'Elle', 151515, 'Romance'),
('Verity', 'Colleen Hoover', 101010, 'Suspense e Misterio'),
('Os Sete Maridos de Evelyn Hugo', 'Taylor Jenkins Reid', 252525, 'Drama e Romance'),
('Corte de Espinhos e Rosas', 'Sarah J Mass', 191919, 'Fantasia'),
('O Verao que Mudou A Minha Vida', 'Jenny Han', 202020, 'Romace'),
('Teto Para Dois', 'Beth O Leary', 335236, 'Romace'),
('It: A Coisa', 'Stephen King', 656565, 'Terror');

INSERT INTO Emprestimos (CpfID, CodigoID, Nome_Cliente, Data_Emprestimo)
VALUES (71569423851, 202020, 'Clara', '2025-09-01'),
('14576235416', 656565, 'Livia', '2025-05-02'),
('12396548725', 121212, 'Amanda', '2025-02-10'),
('32165498700', 141414, 'Julia', '2025-03-06'),
('45678912345', 101010, 'Tainara', '2025-09-07'),
('95135725850', 335236, 'Tays', '2025-09-04'),
('15935748620', 131313, 'Gabriela', '2025-06-20'),
('75395185200', 151515, 'Maria', '2025-09-05'),
('85296374145', 252525, 'Isabela', '2025-01-09'),
('98765432171', 191919, 'Luiza', '2025-08-14');

UPDATE Emprestimos
SET Nome_Cliente = 'Clara'
WHERE CodigoID = 335236;


SELECT Titulo, Autor, CodigoID, Genero
FROM Livros
Where genero LIKE '%Fantasia%';


SELECT COUNT(*) AS total_livros, 
MIN(CodigoID) AS livro_com_menor_codigo,
MAX(CodigoID) AS livro_com_maior_codigo
FROM Livros;

SELECT COUNT(*) AS total_emprestimos,
MIN(Data_Emprestimo) AS primeiro_emprestimo,
MAX(Data_Emprestimo) AS ultimo_emprestimo
FROM Emprestimos;

SELECT Genero, COUNT(*) AS quantidade_livros
FROM Livros
GROUP BY Genero; 

SELECT Data_emprestimo, COUNT(*) AS quantidade_emprestimos
FROM Emprestimos
GROUP BY Data_Emprestimo;

SELECT e.CpfID, e.Nome_Cliente, e.Data_Emprestimo,
       l.Titulo, l.Autor, l.Genero
FROM Emprestimos e
JOIN Livros l ON e.CodigoID = l.CodigoID
ORDER BY e.Nome_Cliente;


SELECT * FROM Livros;
SELECT * FROM Emprestimos;
