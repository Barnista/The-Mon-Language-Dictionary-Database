export const DBPayload = {
    init: (db) => {
        let data = {
            ['author']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/author_1.js');
                    db.run(a1.default);
                }
            },
            ['category']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/category_1.js');
                    db.run(a1.default);
                }
            },
            ['categorydetail']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/categorydetail_1.js');
                    db.run(a1.default);
                }
            },
            ['wordROW1']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/wordROW1_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/wordROW1_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/wordROW1_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/wordROW1_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/wordROW1_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/wordROW1_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/wordROW1_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/wordROW1_8.js');
                    db.run(a8.default);
                    const a9 = await import('../data/wordROW1_9.js');
                    db.run(a9.default);
                    const a10 = await import('../data/wordROW1_10.js');
                    db.run(a10.default);
                }
            },
            ['wordROW2']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/wordROW2_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/wordROW2_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/wordROW2_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/wordROW2_4.js');
                    db.run(a4.default);
                }
            },
            ['wordROW3']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/wordROW3_1.js');
                    db.run(a1.default);
                }
            },
            ['wordROW4']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/wordROW4_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/wordROW4_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/wordROW4_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/wordROW4_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/wordROW4_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/wordROW4_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/wordROW4_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/wordROW4_8.js');
                    db.run(a8.default);
                }
            },
            ['wordROW5']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/wordROW5_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/wordROW5_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/wordROW5_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/wordROW5_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/wordROW5_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/wordROW5_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/wordROW5_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/wordROW5_8.js');
                    db.run(a8.default);
                    const a9 = await import('../data/wordROW5_9.js');
                    db.run(a9.default);
                    const a10 = await import('../data/wordROW5_10.js');
                    db.run(a10.default);
                }
            },
            ['wordROW6']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/wordROW6_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/wordROW6_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/wordROW6_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/wordROW6_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/wordROW6_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/wordROW6_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/wordROW6_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/wordROW6_8.js');
                    db.run(a8.default);
                    const a9 = await import('../data/wordROW6_9.js');
                    db.run(a9.default);
                    const a10 = await import('../data/wordROW6_10.js');
                    db.run(a10.default);
                }
            },
            ['wordROW7']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/wordROW7_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/wordROW7_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/wordROW7_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/wordROW7_4.js');
                    db.run(a4.default);
                }
            },
            ['wordROWVowel']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/wordROWVowel_1.js');
                    db.run(a1.default);
                }
            },
            ['definitionENGROW1']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionENGROW1_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionENGROW1_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionENGROW1_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionENGROW1_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/definitionENGROW1_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/definitionENGROW1_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/definitionENGROW1_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/definitionENGROW1_8.js');
                    db.run(a8.default);
                }
            },
            ['definitionENGROW2']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionENGROW2_1.js');
                    db.run(a1.default);
                }
            },
            ['definitionENGROW3']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionENGROW3_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionENGROW3_2.js');
                    db.run(a2.default);
                }
            },
            ['definitionENGROW4']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionENGROW4_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionENGROW4_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionENGROW4_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionENGROW4_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/definitionENGROW4_5.js');
                    db.run(a5.default);
                }
            },
            ['definitionENGROW5']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionENGROW5_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionENGROW5_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionENGROW5_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionENGROW5_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/definitionENGROW5_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/definitionENGROW5_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/definitionENGROW5_7.js');
                    db.run(a7.default);
                }
            },
            ['definitionENGROW6']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionENGROW6_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionENGROW6_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionENGROW6_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionENGROW6_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/definitionENGROW6_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/definitionENGROW6_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/definitionENGROW6_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/definitionENGROW6_8.js');
                    db.run(a8.default);
                    const a9 = await import('../data/definitionENGROW6_9.js');
                    db.run(a9.default);
                    const a10 = await import('../data/definitionENGROW6_10.js');
                    db.run(a10.default);
                }
            },
            ['definitionENGROW7']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionENGROW7_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionENGROW7_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionENGROW7_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionENGROW7_4.js');
                    db.run(a4.default);
                }
            },
            ['definitionENGROWVowel']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionENGROWVowel_1.js');
                    db.run(a1.default);
                }
            },
            ['definitionTHAROW1']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionTHAROW1_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionTHAROW1_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionTHAROW1_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionTHAROW1_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/definitionTHAROW1_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/definitionTHAROW1_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/definitionTHAROW1_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/definitionTHAROW1_8.js');
                    db.run(a8.default);
                    const a9 = await import('../data/definitionTHAROW1_9.js');
                    db.run(a9.default);
                    const a10 = await import('../data/definitionTHAROW1_10.js');
                    db.run(a10.default);
                    const a11 = await import('../data/definitionTHAROW1_11.js');
                    db.run(a11.default);
                    const a12 = await import('../data/definitionTHAROW1_12.js');
                    db.run(a12.default);
                }
            },
            ['definitionTHAROW2']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionTHAROW2_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionTHAROW2_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionTHAROW2_3.js');
                    db.run(a3.default);
                }
            },
            ['definitionTHAROW3']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionTHAROW3_1.js');
                    db.run(a1.default);
                }
            },
            ['definitionTHAROW4']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionTHAROW4_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionTHAROW4_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionTHAROW4_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionTHAROW4_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/definitionTHAROW4_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/definitionTHAROW4_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/definitionTHAROW4_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/definitionTHAROW4_8.js');
                    db.run(a8.default);
                }
            },
            ['definitionTHAROW5']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionTHAROW5_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionTHAROW5_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionTHAROW5_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionTHAROW5_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/definitionTHAROW5_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/definitionTHAROW5_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/definitionTHAROW5_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/definitionTHAROW5_8.js');
                    db.run(a8.default);
                    const a9 = await import('../data/definitionTHAROW5_9.js');
                    db.run(a9.default);
                    const a10 = await import('../data/definitionTHAROW5_10.js');
                    db.run(a10.default);
                    const a11 = await import('../data/definitionTHAROW5_11.js');
                    db.run(a11.default);
                }
            },
            ['definitionTHAROW6']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionTHAROW6_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionTHAROW6_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionTHAROW6_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionTHAROW6_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/definitionTHAROW6_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/definitionTHAROW6_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/definitionTHAROW6_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/definitionTHAROW6_8.js');
                    db.run(a8.default);
                    const a9 = await import('../data/definitionTHAROW6_9.js');
                    db.run(a9.default);
                    const a10 = await import('../data/definitionTHAROW6_10.js');
                    db.run(a10.default);
                    const a11 = await import('../data/definitionTHAROW6_11.js');
                    db.run(a11.default);
                    const a12 = await import('../data/definitionTHAROW6_12.js');
                    db.run(a12.default);
                    const a13 = await import('../data/definitionTHAROW6_13.js');
                    db.run(a13.default);
                    const a14 = await import('../data/definitionTHAROW6_14.js');
                    db.run(a14.default);
                    const a15 = await import('../data/definitionTHAROW6_15.js');
                    db.run(a15.default);
                }
            },
            ['definitionTHAROW7']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionTHAROW7_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionTHAROW7_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionTHAROW7_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionTHAROW7_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/definitionTHAROW7_5.js');
                    db.run(a5.default);
                }
            },
            ['definitionTHAROWVowel']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionTHAROWVowel_1.js');
                    db.run(a1.default);
                }
            },
            ['definitionMYAROW1']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionMYAROW1_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionMYAROW1_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionMYAROW1_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionMYAROW1_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/definitionMYAROW1_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/definitionMYAROW1_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/definitionMYAROW1_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/definitionMYAROW1_8.js');
                    db.run(a8.default);
                    const a9 = await import('../data/definitionMYAROW1_9.js');
                    db.run(a9.default);
                    const a10 = await import('../data/definitionMYAROW1_10.js');
                    db.run(a10.default);
                    const a11 = await import('../data/definitionMYAROW1_11.js');
                    db.run(a11.default);
                }
            },
            ['definitionMYAROW2']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionMYAROW2_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionMYAROW2_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionMYAROW2_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionMYAROW2_4.js');
                    db.run(a4.default);
                }
            },
            ['definitionMYAROW3']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionMYAROW3_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionMYAROW3_2.js');
                    db.run(a2.default);
                }
            },
            ['definitionMYAROW4']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionMYAROW4_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionMYAROW4_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionMYAROW4_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionMYAROW4_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/definitionMYAROW4_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/definitionMYAROW4_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/definitionMYAROW4_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/definitionMYAROW4_8.js');
                    db.run(a8.default);
                    const a9 = await import('../data/definitionMYAROW4_9.js');
                    db.run(a9.default);
                }
            },
            ['definitionMYAROW5']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionMYAROW5_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionMYAROW5_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionMYAROW5_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionMYAROW5_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/definitionMYAROW5_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/definitionMYAROW5_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/definitionMYAROW5_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/definitionMYAROW5_8.js');
                    db.run(a8.default);
                    const a9 = await import('../data/definitionMYAROW5_9.js');
                    db.run(a9.default);
                    const a10 = await import('../data/definitionMYAROW5_10.js');
                    db.run(a10.default);
                    const a11 = await import('../data/definitionMYAROW5_11.js');
                    db.run(a11.default);
                }
            },
            ['definitionMYAROW6']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionMYAROW6_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionMYAROW6_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionMYAROW6_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionMYAROW6_4.js');
                    db.run(a4.default);
                    const a5 = await import('../data/definitionMYAROW6_5.js');
                    db.run(a5.default);
                    const a6 = await import('../data/definitionMYAROW6_6.js');
                    db.run(a6.default);
                    const a7 = await import('../data/definitionMYAROW6_7.js');
                    db.run(a7.default);
                    const a8 = await import('../data/definitionMYAROW6_8.js');
                    db.run(a8.default);
                    const a9 = await import('../data/definitionMYAROW6_9.js');
                    db.run(a9.default);
                    const a10 = await import('../data/definitionMYAROW6_10.js');
                    db.run(a10.default);
                    const a11 = await import('../data/definitionMYAROW6_11.js');
                    db.run(a11.default);
                }
            },
            ['definitionMYAROW7']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionMYAROW7_1.js');
                    db.run(a1.default);
                    const a2 = await import('../data/definitionMYAROW7_2.js');
                    db.run(a2.default);
                    const a3 = await import('../data/definitionMYAROW7_3.js');
                    db.run(a3.default);
                    const a4 = await import('../data/definitionMYAROW7_4.js');
                    db.run(a4.default);
                }
            },
            ['definitionMYAROWVowel']: {
                isLoaded: false,
                load: async () => {
                    const a1 = await import('../data/definitionMYAROWVowel_1.js');
                    db.run(a1.default);
                }
            },
        };
        return {
            db: db,
            data: data,
            isLoaded: (keyName) => {
                return (data[keyName].isLoaded)
            },
            loadAsync: async (keyName) => {
                let milisec = 0;
                const clock = setInterval(() => {
                    milisec++;
                }, 1);

                // ASYNC LOADING DATA
                if (!data[keyName].isLoaded) {
                    await data[keyName].load();
                    data[keyName].isLoaded = true;
                }

                clearInterval(clock)
                return milisec;
            },
        }
    },
    loadFromWord: async (payload, word, lang_code) => {
        const char = word[0];
        const ROW1 = ['က', 'ခ', 'ဂ', 'ဃ', 'ၚ'];
        const ROW2 = ['စ', 'ဆ', 'ဇ', 'ၛ', 'ည'];
        const ROW3 = ['ဋ', 'ဌ', 'ဍ', 'ဎ', 'ဏ'];
        const ROW4 = ['တ', 'ထ', 'ဒ', 'ဓ', 'န'];
        const ROW5 = ['ပ', 'ဖ', 'ဗ', 'ဘ', 'မ'];
        const ROW6 = ['ယ', 'ရ', 'လ', 'ဝ', 'သ'];
        const ROW7 = ['ဟ', 'ဠ', 'ၜ', 'အ', 'ၝ'];
        const ROWVowel = ['ဣ', 'ဥ', 'ဨ', 'ဩ'];

        let mil = 0;
        if (ROW1.includes(char)) {
            mil = mil + await payload.loadAsync(`wordROW1`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW1`);
        } else if (ROW2.includes(char)) {
            mil = mil + await payload.loadAsync(`wordROW2`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW2`);
        } else if (ROW3.includes(char)) {
            mil = mil + await payload.loadAsync(`wordROW3`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW3`);
        } else if (ROW4.includes(char)) {
            mil = mil + await payload.loadAsync(`wordROW4`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW4`);
        } else if (ROW5.includes(char)) {
            mil = mil + await payload.loadAsync(`wordROW5`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW5`);
        } else if (ROW6.includes(char)) {
            mil = mil + await payload.loadAsync(`wordROW6`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW6`);
        } else if (ROW7.includes(char)) {
            mil = mil + await payload.loadAsync(`wordROW7`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW7`);
        } else if (ROWVowel.includes(char)) {
            mil = mil + await payload.loadAsync(`wordROWVowel`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROWVowel`);
        } else {
            mil = mil + await payload.loadAsync(`wordROW1`);
            mil = mil + await payload.loadAsync(`wordROW2`);
            mil = mil + await payload.loadAsync(`wordROW3`);
            mil = mil + await payload.loadAsync(`wordROW4`);
            mil = mil + await payload.loadAsync(`wordROW5`);
            mil = mil + await payload.loadAsync(`wordROW6`);
            mil = mil + await payload.loadAsync(`wordROW7`);
            mil = mil + await payload.loadAsync(`wordROWVowel`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW1`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW2`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW3`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW4`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW5`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW6`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW7`);
            mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROWVowel`);
        }

        return mil;
    },
    loadFromDefinition: async (payload, lang_code) => {
        let mil = 0;
        mil = mil + await payload.loadAsync(`wordROW1`);
        mil = mil + await payload.loadAsync(`wordROW2`);
        mil = mil + await payload.loadAsync(`wordROW3`);
        mil = mil + await payload.loadAsync(`wordROW4`);
        mil = mil + await payload.loadAsync(`wordROW5`);
        mil = mil + await payload.loadAsync(`wordROW6`);
        mil = mil + await payload.loadAsync(`wordROW7`);
        mil = mil + await payload.loadAsync(`wordROWVowel`);
        mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW1`);
        mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW2`);
        mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW3`);
        mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW4`);
        mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW5`);
        mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW6`);
        mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROW7`);
        mil = mil + await payload.loadAsync(`definition${lang_code.toUpperCase()}ROWVowel`);
        return mil;
    }
}