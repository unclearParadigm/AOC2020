fs = require('fs');

function firstOrDefault(arr, def) {
    return (arr.length == 0) ? def : arr[0];
}

function hasAllFields(pp) {
    return pp.hgt != '' && pp.iyr != 0 && pp.hcl != '' && pp.byr != 0 && pp.ecl != '' && pp.eyr != 0 && pp.pid != '';
}

function isValidPassport(pp) {
    if(pp.byr < 1920 || pp.byr > 2002) return false;
    if(pp.iyr < 2010 || pp.iyr > 2020) return false;
    if(pp.eyr < 2020 || pp.eyr > 2030) return false;

    const isHeightInCm = pp.hgt.indexOf('cm') > -1;
    const isHeightInInch = pp.hgt.indexOf('in') > -1;
    if(!isHeightInCm && !isHeightInInch) return false;
    const height = parseInt(pp.hgt.replace('in', '').replace('cm', ''));
    if(isHeightInInch && (height < 59 || height > 76)) return false;
    if(isHeightInCm && (height < 150 || height > 193)) return false;
    
    if(pp.pid.length != 9) return false;
    if(!pp.hcl.startsWith('#') || pp.hcl.length != 7 || !pp.hcl.match('[a-f0-9]*')) return false;
    if(!['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].map(vec => pp.ecl == vec).reduce((x, y) => x || y)) return false;
    return true;
}
    
fs.readFile('aoc2020_04_input.txt', 'utf-8', function(err, data) {
    let passport = [];
    let passports = [];
    let linesplit = data.split('\n');

    for(var l = 0; l < linesplit.length; l++) {
        if(linesplit[l] == '') {
            var passport_split = passport.join(' ').split(' ');
            passports.push({
                hgt: firstOrDefault(passport_split.filter(v => v.startsWith('hgt')), '').replace('hgt:', ''),
                iyr: parseInt(firstOrDefault(passport_split.filter(v => v.startsWith('iyr')), '0').replace('iyr:', '')),
                hcl: firstOrDefault(passport_split.filter(v => v.startsWith('hcl')), '').replace('hcl:', ''),
                ecl: firstOrDefault(passport_split.filter(v => v.startsWith('ecl')), '').replace('ecl:', ''),
                byr: parseInt(firstOrDefault(passport_split.filter(v => v.startsWith('byr')), '0').replace('byr:', '')),
                eyr: parseInt(firstOrDefault(passport_split.filter(v => v.startsWith('eyr')), '0').replace('eyr:', '')),
                cid: firstOrDefault(passport_split.filter(v => v.startsWith('cid')), '').replace('cid:', ''),
                pid: firstOrDefault(passport_split.filter(v => v.startsWith('pid')), '').replace('pid:', '')
            });
            passport = [];
            continue;
        }
        else {
            passport.push(linesplit[l]);
        }
    }
    
    console.log('All Passports: ', passports.length);
    console.log('Part 1: ', passports.filter(pp => hasAllFields(pp)).length);
    console.log('Part 2: ', passports.filter(pp => hasAllFields(pp) && isValidPassport(pp)).length);
});