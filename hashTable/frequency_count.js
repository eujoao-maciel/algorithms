const palavra = "programing";

const frequency_count = (palavra) => {
  const letras = {};

  for (let i = 0; i < palavra.length; i++) {
    const char = palavra[i]

    if (letras[char]) {
      letras[char] += 1;
    } else {
      letras[char] = 1;
    }
  }

  return letras;
};

console.log(frequency_count(palavra));
