#SQL COMMAND FOR DELETE EVERY WORDS EXCEPT ...CONDITION...
DELETE FROM `WordROW1`
WHERE `word` NOT LIKE 'က%' 
AND `word` NOT LIKE 'ခ%' 
AND `word` NOT LIKE 'ဂ%' 
AND `word` NOT LIKE 'ဃ%' 
AND `word` NOT LIKE 'ၚ%'


DELETE FROM `WordROW2`
WHERE `word` NOT LIKE 'စ%' 
AND `word` NOT LIKE 'ဆ%' 
AND `word` NOT LIKE 'ဇ%' 
AND `word` NOT LIKE 'ၛ%' 
AND `word` NOT LIKE 'ည%'

DELETE FROM `WordROW3`
WHERE `word` NOT LIKE 'ဋ%' 
AND `word` NOT LIKE 'ဌ%' 
AND `word` NOT LIKE 'ဍ%' 
AND `word` NOT LIKE 'ဎ%' 
AND `word` NOT LIKE 'ဏ%'

DELETE FROM `WordROW4`
WHERE `word` NOT LIKE 'တ%' 
AND `word` NOT LIKE 'ထ%' 
AND `word` NOT LIKE 'ဒ%' 
AND `word` NOT LIKE 'ဓ%' 
AND `word` NOT LIKE 'န%'

DELETE FROM `WordROW5`
WHERE `word` NOT LIKE 'ပ%' 
AND `word` NOT LIKE 'ဖ%' 
AND `word` NOT LIKE 'ဗ%' 
AND `word` NOT LIKE 'ဘ%' 
AND `word` NOT LIKE 'မ%'

DELETE FROM `WordROW6`
WHERE `word` NOT LIKE 'ယ%' 
AND `word` NOT LIKE 'ရ%' 
AND `word` NOT LIKE 'လ%' 
AND `word` NOT LIKE 'ဝ%' 
AND `word` NOT LIKE 'သ%'

DELETE FROM `WordROW7`
WHERE `word` NOT LIKE 'ဟ%' 
AND `word` NOT LIKE 'ဠ%' 
AND `word` NOT LIKE 'ၜ%' 
AND `word` NOT LIKE 'အ%' 
AND `word` NOT LIKE 'ၝ%'




#SQL COMMANDS FOR DELETE EVERY DEFINITIONS EXCEPT ....CONDITION....
DELETE FROM `DefinitionENGROW6` 
WHERE `word_id`
NOT IN (SELECT `id` FROM `WordROW6`)

DELETE FROM `DefinitionTHAROW1` 
WHERE `word_id`
NOT IN (SELECT `id` FROM `WordROW1`)

DELETE FROM `DefinitionMYAROW1` 
WHERE `word_id`
NOT IN (SELECT `id` FROM `WordROW1`)