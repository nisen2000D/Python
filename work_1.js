function getDigitsOfNum(num) {
    if (!Number.isInteger(num) || num > 999) {
        console.log('Значение должно быть от 0 до 999.');
        return {};
    }

    return {
        units: num % 10,
        hundereds: Math.floor(num / 100),
        tens: Math.floor(num / 10) % 10,
    }
}

console.log(getDigitsOfNum(123));