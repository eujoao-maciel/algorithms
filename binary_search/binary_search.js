const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const binary_search = (array, choiceItem) => {
  let inicio = 0;
  let fim = numeros.length - 1;

  while (inicio <= fim) {
    let meio = Math.floor((inicio + fim) / 2);
    let item = array[meio];

    if (item === choiceItem) {
      return item;
    }

    if (item > choiceItem) {
      fim = meio - 1;
      console.log(`fim = meio:${meio} - 1`)
    }

    if (item < choiceItem) {
      inicio = meio + 1;
      console.log(`inicio = meio:${meio} + 1`)
    }
  }

  return null;
};

console.log(binary_search(numeros, 10));
