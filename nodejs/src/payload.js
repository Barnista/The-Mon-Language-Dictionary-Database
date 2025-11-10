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
            ['word']: {
                isLoaded: false,
                load: async () => {
                    const w1 = await import('../data/word_1.js');
                    db.run(w1.default);
                    const w2 = await import('../data/word_2.js');
                    db.run(w2.default);
                    const w3 = await import('../data/word_3.js');
                    db.run(w3.default);
                    const w4 = await import('../data/word_4.js');
                    db.run(w4.default);
                    const w5 = await import('../data/word_5.js');
                    db.run(w5.default);
                    const w6 = await import('../data/word_6.js');
                    db.run(w6.default);
                    const w7 = await import('../data/word_7.js');
                    db.run(w7.default);
                    const w8 = await import('../data/word_8.js');
                    db.run(w8.default);
                    const w9 = await import('../data/word_9.js');
                    db.run(w9.default);
                    const w10 = await import('../data/word_10.js');
                    db.run(w10.default);
                    const w11 = await import('../data/word_11.js');
                    db.run(w11.default);
                    const w12 = await import('../data/word_12.js');
                    db.run(w12.default);
                    const w13 = await import('../data/word_13.js');
                    db.run(w13.default);
                    const w14 = await import('../data/word_14.js');
                    db.run(w14.default);
                    const w15 = await import('../data/word_15.js');
                    db.run(w15.default);
                    const w16 = await import('../data/word_16.js');
                    db.run(w16.default);
                    const w17 = await import('../data/word_17.js');
                    db.run(w17.default);
                    const w18 = await import('../data/word_18.js');
                    db.run(w18.default);
                    const w19 = await import('../data/word_19.js');
                    db.run(w19.default);
                    const w20 = await import('../data/word_20.js');
                    db.run(w20.default);
                    const w21 = await import('../data/word_21.js');
                    db.run(w21.default);
                    const w22 = await import('../data/word_22.js');
                    db.run(w22.default);
                    const w23 = await import('../data/word_23.js');
                    db.run(w23.default);
                    const w24 = await import('../data/word_24.js');
                    db.run(w24.default);
                    const w25 = await import('../data/word_25.js');
                    db.run(w25.default);
                    const w26 = await import('../data/word_26.js');
                    db.run(w26.default);
                    const w27 = await import('../data/word_27.js');
                    db.run(w27.default);
                    const w28 = await import('../data/word_28.js');
                    db.run(w28.default);
                    const w29 = await import('../data/word_29.js');
                    db.run(w29.default);
                    const w30 = await import('../data/word_30.js');
                    db.run(w30.default);
                    const w31 = await import('../data/word_31.js');
                    db.run(w31.default);
                    const w32 = await import('../data/word_32.js');
                    db.run(w32.default);
                    const w33 = await import('../data/word_33.js');
                    db.run(w33.default);
                    const w34 = await import('../data/word_34.js');
                    db.run(w34.default);
                    const w35 = await import('../data/word_35.js');
                    db.run(w35.default);
                    const w36 = await import('../data/word_36.js');
                    db.run(w36.default);
                    const w37 = await import('../data/word_37.js');
                    db.run(w37.default);
                    const w38 = await import('../data/word_38.js');
                    db.run(w38.default);
                    const w39 = await import('../data/word_39.js');
                    db.run(w39.default);
                    const w40 = await import('../data/word_40.js');
                    db.run(w40.default);
                    const w41 = await import('../data/word_41.js');
                    db.run(w41.default);
                    const w42 = await import('../data/word_42.js');
                    db.run(w42.default);
                }
            },
            ['definitionENG']: {
                isLoaded: false,
                load: async () => {
                    const d1 = await import('../data/definitionENG_1.js');
                    db.run(d1.default);
                    const d2 = await import('../data/definitionENG_2.js');
                    db.run(d2.default);
                    const d3 = await import('../data/definitionENG_3.js');
                    db.run(d3.default);
                    const d4 = await import('../data/definitionENG_4.js');
                    db.run(d4.default);
                    const d5 = await import('../data/definitionENG_5.js');
                    db.run(d5.default);
                    const d6 = await import('../data/definitionENG_6.js');
                    db.run(d6.default);
                    const d7 = await import('../data/definitionENG_7.js');
                    db.run(d7.default);
                    const d8 = await import('../data/definitionENG_8.js');
                    db.run(d8.default);
                    const d9 = await import('../data/definitionENG_9.js');
                    db.run(d9.default);
                    const d10 = await import('../data/definitionENG_10.js');
                    db.run(d10.default);
                    const d11 = await import('../data/definitionENG_11.js');
                    db.run(d11.default);
                    const d12 = await import('../data/definitionENG_12.js');
                    db.run(d12.default);
                    const d13 = await import('../data/definitionENG_13.js');
                    db.run(d13.default);
                    const d14 = await import('../data/definitionENG_14.js');
                    db.run(d14.default);
                    const d15 = await import('../data/definitionENG_15.js');
                    db.run(d15.default);
                    const d16 = await import('../data/definitionENG_16.js');
                    db.run(d16.default);
                    const d17 = await import('../data/definitionENG_17.js');
                    db.run(d17.default);
                    const d18 = await import('../data/definitionENG_18.js');
                    db.run(d18.default);
                    const d19 = await import('../data/definitionENG_19.js');
                    db.run(d19.default);
                    const d20 = await import('../data/definitionENG_20.js');
                    db.run(d20.default);
                    const d21 = await import('../data/definitionENG_21.js');
                    db.run(d21.default);
                    const d22 = await import('../data/definitionENG_22.js');
                    db.run(d22.default);
                    const d23 = await import('../data/definitionENG_23.js');
                    db.run(d23.default);
                    const d24 = await import('../data/definitionENG_24.js');
                    db.run(d24.default);
                    const d25 = await import('../data/definitionENG_25.js');
                    db.run(d25.default);
                    const d26 = await import('../data/definitionENG_26.js');
                    db.run(d26.default);
                    const d27 = await import('../data/definitionENG_27.js');
                    db.run(d27.default);
                    const d28 = await import('../data/definitionENG_28.js');
                    db.run(d28.default);
                    const d29 = await import('../data/definitionENG_29.js');
                    db.run(d29.default);
                    const d30 = await import('../data/definitionENG_30.js');
                    db.run(d30.default);
                    const d31 = await import('../data/definitionENG_31.js');
                    db.run(d31.default);
                    const d32 = await import('../data/definitionENG_32.js');
                    db.run(d32.default);
                    const d33 = await import('../data/definitionENG_33.js');
                    db.run(d33.default);
                    const d34 = await import('../data/definitionENG_34.js');
                    db.run(d34.default);
                    const d35 = await import('../data/definitionENG_35.js');
                    db.run(d35.default);
                    const d36 = await import('../data/definitionENG_36.js');
                    db.run(d36.default);
                    const d37 = await import('../data/definitionENG_37.js');
                    db.run(d37.default);
                }
            },
            ['definitionTHA']: {
                isLoaded: false,
                load: async () => {
                    const d1 = await import('../data/definitionTHA_1.js');
                    db.run(d1.default);
                    const d2 = await import('../data/definitionTHA_2.js');
                    db.run(d2.default);
                    const d3 = await import('../data/definitionTHA_3.js');
                    db.run(d3.default);
                    const d4 = await import('../data/definitionTHA_4.js');
                    db.run(d4.default);
                    const d5 = await import('../data/definitionTHA_5.js');
                    db.run(d5.default);
                    const d6 = await import('../data/definitionTHA_6.js');
                    db.run(d6.default);
                    const d7 = await import('../data/definitionTHA_7.js');
                    db.run(d7.default);
                    const d8 = await import('../data/definitionTHA_8.js');
                    db.run(d8.default);
                    const d9 = await import('../data/definitionTHA_9.js');
                    db.run(d9.default);
                    const d10 = await import('../data/definitionTHA_10.js');
                    db.run(d10.default);
                    const d11 = await import('../data/definitionTHA_11.js');
                    db.run(d11.default);
                    const d12 = await import('../data/definitionTHA_12.js');
                    db.run(d12.default);
                    const d13 = await import('../data/definitionTHA_13.js');
                    db.run(d13.default);
                    const d14 = await import('../data/definitionTHA_14.js');
                    db.run(d14.default);
                    const d15 = await import('../data/definitionTHA_15.js');
                    db.run(d15.default);
                    const d16 = await import('../data/definitionTHA_16.js');
                    db.run(d16.default);
                    const d17 = await import('../data/definitionTHA_17.js');
                    db.run(d17.default);
                    const d18 = await import('../data/definitionTHA_18.js');
                    db.run(d18.default);
                    const d19 = await import('../data/definitionTHA_19.js');
                    db.run(d19.default);
                    const d20 = await import('../data/definitionTHA_20.js');
                    db.run(d20.default);
                    const d21 = await import('../data/definitionTHA_21.js');
                    db.run(d21.default);
                    const d22 = await import('../data/definitionTHA_22.js');
                    db.run(d22.default);
                    const d23 = await import('../data/definitionTHA_23.js');
                    db.run(d23.default);
                    const d24 = await import('../data/definitionTHA_24.js');
                    db.run(d24.default);
                    const d25 = await import('../data/definitionTHA_25.js');
                    db.run(d25.default);
                    const d26 = await import('../data/definitionTHA_26.js');
                    db.run(d26.default);
                    const d27 = await import('../data/definitionTHA_27.js');
                    db.run(d27.default);
                    const d28 = await import('../data/definitionTHA_28.js');
                    db.run(d28.default);
                    const d29 = await import('../data/definitionTHA_29.js');
                    db.run(d29.default);
                    const d30 = await import('../data/definitionTHA_30.js');
                    db.run(d30.default);
                    const d31 = await import('../data/definitionTHA_31.js');
                    db.run(d31.default);
                    const d32 = await import('../data/definitionTHA_32.js');
                    db.run(d32.default);
                    const d33 = await import('../data/definitionTHA_33.js');
                    db.run(d33.default);
                    const d34 = await import('../data/definitionTHA_34.js');
                    db.run(d34.default);
                    const d35 = await import('../data/definitionTHA_35.js');
                    db.run(d35.default);
                    const d36 = await import('../data/definitionTHA_36.js');
                    db.run(d36.default);
                    const d37 = await import('../data/definitionTHA_37.js');
                    db.run(d37.default);
                    const d38 = await import('../data/definitionTHA_38.js');
                    db.run(d38.default);
                    const d39 = await import('../data/definitionTHA_39.js');
                    db.run(d39.default);
                    const d40 = await import('../data/definitionTHA_40.js');
                    db.run(d40.default);
                    const d41 = await import('../data/definitionTHA_41.js');
                    db.run(d41.default);
                    const d42 = await import('../data/definitionTHA_42.js');
                    db.run(d42.default);
                    const d43 = await import('../data/definitionTHA_43.js');
                    db.run(d43.default);
                    const d44 = await import('../data/definitionTHA_44.js');
                    db.run(d44.default);
                    const d45 = await import('../data/definitionTHA_45.js');
                    db.run(d45.default);
                    const d46 = await import('../data/definitionTHA_46.js');
                    db.run(d46.default);
                    const d47 = await import('../data/definitionTHA_47.js');
                    db.run(d47.default);
                    const d48 = await import('../data/definitionTHA_48.js');
                    db.run(d48.default);
                    const d49 = await import('../data/definitionTHA_49.js');
                    db.run(d49.default);
                }
            },
            ['definitionMYA']: {
                isLoaded: false,
                load: async () => {
                    const d1 = await import('../data/definitionMYA_1.js');
                    db.run(d1.default);
                    const d2 = await import('../data/definitionMYA_2.js');
                    db.run(d2.default);
                    const d3 = await import('../data/definitionMYA_3.js');
                    db.run(d3.default);
                    const d4 = await import('../data/definitionMYA_4.js');
                    db.run(d4.default);
                    const d5 = await import('../data/definitionMYA_5.js');
                    db.run(d5.default);
                    const d6 = await import('../data/definitionMYA_6.js');
                    db.run(d6.default);
                    const d7 = await import('../data/definitionMYA_7.js');
                    db.run(d7.default);
                    const d8 = await import('../data/definitionMYA_8.js');
                    db.run(d8.default);
                    const d9 = await import('../data/definitionMYA_9.js');
                    db.run(d9.default);
                    const d10 = await import('../data/definitionMYA_10.js');
                    db.run(d10.default);
                    const d11 = await import('../data/definitionMYA_11.js');
                    db.run(d11.default);
                    const d12 = await import('../data/definitionMYA_12.js');
                    db.run(d12.default);
                    const d13 = await import('../data/definitionMYA_13.js');
                    db.run(d13.default);
                    const d14 = await import('../data/definitionMYA_14.js');
                    db.run(d14.default);
                    const d15 = await import('../data/definitionMYA_15.js');
                    db.run(d15.default);
                    const d16 = await import('../data/definitionMYA_16.js');
                    db.run(d16.default);
                    const d17 = await import('../data/definitionMYA_17.js');
                    db.run(d17.default);
                    const d18 = await import('../data/definitionMYA_18.js');
                    db.run(d18.default);
                    const d19 = await import('../data/definitionMYA_19.js');
                    db.run(d19.default);
                    const d20 = await import('../data/definitionMYA_20.js');
                    db.run(d20.default);
                    const d21 = await import('../data/definitionMYA_21.js');
                    db.run(d21.default);
                    const d22 = await import('../data/definitionMYA_22.js');
                    db.run(d22.default);
                    const d23 = await import('../data/definitionMYA_23.js');
                    db.run(d23.default);
                    const d24 = await import('../data/definitionMYA_24.js');
                    db.run(d24.default);
                    const d25 = await import('../data/definitionMYA_25.js');
                    db.run(d25.default);
                    const d26 = await import('../data/definitionMYA_26.js');
                    db.run(d26.default);
                    const d27 = await import('../data/definitionMYA_27.js');
                    db.run(d27.default);
                    const d28 = await import('../data/definitionMYA_28.js');
                    db.run(d28.default);
                    const d29 = await import('../data/definitionMYA_29.js');
                    db.run(d29.default);
                    const d30 = await import('../data/definitionMYA_30.js');
                    db.run(d30.default);
                    const d31 = await import('../data/definitionMYA_31.js');
                    db.run(d31.default);
                    const d32 = await import('../data/definitionMYA_32.js');
                    db.run(d32.default);
                    const d33 = await import('../data/definitionMYA_33.js');
                    db.run(d33.default);
                    const d34 = await import('../data/definitionMYA_34.js');
                    db.run(d34.default);
                    const d35 = await import('../data/definitionMYA_35.js');
                    db.run(d35.default);
                    const d36 = await import('../data/definitionMYA_36.js');
                    db.run(d36.default);
                    const d37 = await import('../data/definitionMYA_37.js');
                    db.run(d37.default);
                    const d38 = await import('../data/definitionMYA_38.js');
                    db.run(d38.default);
                    const d39 = await import('../data/definitionMYA_39.js');
                    db.run(d39.default);
                    const d40 = await import('../data/definitionMYA_40.js');
                    db.run(d40.default);
                    const d41 = await import('../data/definitionMYA_41.js');
                    db.run(d41.default);
                    const d42 = await import('../data/definitionMYA_42.js');
                    db.run(d42.default);
                    const d43 = await import('../data/definitionMYA_43.js');
                    db.run(d43.default);
                    const d44 = await import('../data/definitionMYA_44.js');
                    db.run(d44.default);
                    const d45 = await import('../data/definitionMYA_45.js');
                    db.run(d45.default);
                    const d46 = await import('../data/definitionMYA_46.js');
                    db.run(d46.default);
                    const d47 = await import('../data/definitionMYA_47.js');
                    db.run(d47.default);
                    const d48 = await import('../data/definitionMYA_48.js');
                    db.run(d48.default);
                    const d49 = await import('../data/definitionMYA_49.js');
                    db.run(d49.default);
                    const d50 = await import('../data/definitionMYA_50.js');
                    db.run(d50.default);
                    const d51 = await import('../data/definitionMYA_51.js');
                    db.run(d51.default);
                }
            }
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
}