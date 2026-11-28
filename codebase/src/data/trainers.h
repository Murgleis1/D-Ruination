//
// DO NOT MODIFY THIS FILE! It is auto-generated from src/data/trainers.party
//
// If you want to modify this file set COMPETITIVE_PARTY_SYNTAX to FALSE
// in include/config/general.h and remove this notice.
// Use sed -i '/^#line/d' 'src/data/trainers.h' to remove #line markers.
//

#line 1 "src/data/trainers.party"

#line 80
    [DIFFICULTY_NORMAL][TRAINER_NONE] =
    {
#line 82
        .trainerClass = TRAINER_CLASS_YOUNGSTER,
#line 83
        .trainerPic = TRAINER_PIC_HIKER,
        .encounterMusic_gender =
#line 85
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 86
        .doubleBattle = FALSE,
        .partySize = 0,
        .party = (const struct TrainerMon[])
        {
        },
    },
#line 89
#line 91
    [DIFFICULTY_EASY][TRAINER_ROUTE1_A] =
    {
#line 90
        .trainerName = _("Jose"),
#line 92
        .trainerClass = TRAINER_CLASS_YOUNGSTER,
#line 93
        .trainerPic = TRAINER_PIC_YOUNGSTER,
        .encounterMusic_gender =
#line 95
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 96
        .doubleBattle = FALSE,
#line 97
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 99
            .species = SPECIES_RATTATA_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 101
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 100
            .lvl = 3,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 103
#line 105
    [DIFFICULTY_NORMAL][TRAINER_ROUTE1_A] =
    {
#line 104
        .trainerName = _("Jose"),
#line 106
        .trainerClass = TRAINER_CLASS_YOUNGSTER,
#line 107
        .trainerPic = TRAINER_PIC_YOUNGSTER,
        .encounterMusic_gender =
#line 109
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 110
        .doubleBattle = FALSE,
#line 111
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 113
            .species = SPECIES_RATTATA_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 115
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 114
            .lvl = 3,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 116
#line 117
    [DIFFICULTY_EASY][TRAINER_ROUTE1_B] =
    {
#line 118
        .trainerName = _("Sana"),
#line 119
        .trainerClass = TRAINER_CLASS_LASS,
#line 120
        .trainerPic = TRAINER_PIC_LASS,
        .encounterMusic_gender =
#line 121
F_TRAINER_FEMALE | 
#line 122
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 123
        .doubleBattle = FALSE,
#line 124
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 126
            .species = SPECIES_PIDOVE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 128
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 127
            .lvl = 3,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 131
#line 133
    [DIFFICULTY_NORMAL][TRAINER_ROUTE1_B] =
    {
#line 132
        .trainerName = _("Sana"),
#line 134
        .trainerClass = TRAINER_CLASS_LASS,
#line 135
        .trainerPic = TRAINER_PIC_LASS,
        .encounterMusic_gender =
#line 136
F_TRAINER_FEMALE | 
#line 137
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 138
        .doubleBattle = FALSE,
#line 139
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 141
            .species = SPECIES_PIDOVE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 143
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 142
            .lvl = 3,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 145
#line 147
    [DIFFICULTY_EASY][TRAINER_ROUTE1_C] =
    {
#line 146
        .trainerName = _("Manya"),
#line 148
        .trainerClass = TRAINER_CLASS_BUG_CATCHER_F,
#line 149
        .trainerPic = TRAINER_PIC_BUG_CATCHER_F,
        .encounterMusic_gender =
#line 151
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 152
        .doubleBattle = FALSE,
#line 153
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 155
            .species = SPECIES_BLIPBUG,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 157
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 156
            .lvl = 2,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 159
            .species = SPECIES_NYMBLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 161
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 160
            .lvl = 3,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 164
#line 166
    [DIFFICULTY_NORMAL][TRAINER_ROUTE1_C] =
    {
#line 165
        .trainerName = _("Manya"),
#line 167
        .trainerClass = TRAINER_CLASS_BUG_CATCHER_F,
#line 168
        .trainerPic = TRAINER_PIC_BUG_CATCHER_F,
        .encounterMusic_gender =
#line 170
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 171
        .doubleBattle = FALSE,
#line 172
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 174
            .species = SPECIES_BLIPBUG,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 176
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 175
            .lvl = 2,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 177
            .species = SPECIES_NYMBLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 179
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 178
            .lvl = 3,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 181
#line 183
    [DIFFICULTY_EASY][TRAINER_KOHLA_LAB] =
    {
#line 182
        .trainerName = _("Kohla"),
#line 184
        .trainerClass = TRAINER_CLASS_ACE_ROOKIE,
#line 185
        .trainerPic = TRAINER_PIC_WALLY,
        .encounterMusic_gender =
#line 187
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 188
        .doubleBattle = FALSE,
#line 189
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
#line 190
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 192
            .species = SPECIES_CHARCADET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 194
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 193
            .lvl = 7,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 196
#line 198
    [DIFFICULTY_NORMAL][TRAINER_KOHLA_LAB] =
    {
#line 197
        .trainerName = _("Kohla"),
#line 199
        .trainerClass = TRAINER_CLASS_ACE_ROOKIE,
#line 200
        .trainerPic = TRAINER_PIC_WALLY,
        .encounterMusic_gender =
#line 202
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 203
        .doubleBattle = FALSE,
#line 204
        .aiFlags = AI_FLAG_SMART_TRAINER,
#line 205
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 207
            .species = SPECIES_CHARCADET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 209
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 208
            .lvl = 7,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 211
#line 213
    [DIFFICULTY_EASY][TRAINER_ROUTE3_JANA] =
    {
#line 212
        .trainerName = _("Jana"),
#line 214
        .trainerClass = TRAINER_CLASS_PKMN_BREEDER,
#line 215
        .trainerPic = TRAINER_PIC_POKEMON_BREEDER_F,
        .encounterMusic_gender =
#line 216
F_TRAINER_FEMALE | 
#line 217
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 218
        .doubleBattle = FALSE,
#line 219
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 221
            .species = SPECIES_FENNEKIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 223
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 222
            .lvl = 7,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 225
            .species = SPECIES_VULPIX_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 227
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 226
            .lvl = 7,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 229
#line 231
    [DIFFICULTY_NORMAL][TRAINER_ROUTE3_JANA] =
    {
#line 230
        .trainerName = _("Jana"),
#line 232
        .trainerClass = TRAINER_CLASS_PKMN_BREEDER,
#line 233
        .trainerPic = TRAINER_PIC_POKEMON_BREEDER_F,
        .encounterMusic_gender =
#line 234
F_TRAINER_FEMALE | 
#line 235
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 236
        .doubleBattle = FALSE,
#line 237
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 239
            .species = SPECIES_FENNEKIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 241
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 240
            .lvl = 7,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 242
            .species = SPECIES_VULPIX_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 244
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 243
            .lvl = 7,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 247
#line 249
    [DIFFICULTY_EASY][TRAINER_ROUTE3_KIM] =
    {
#line 248
        .trainerName = _("Kim"),
#line 250
        .trainerClass = TRAINER_CLASS_LASS,
#line 251
        .trainerPic = TRAINER_PIC_LASS,
        .encounterMusic_gender =
#line 252
F_TRAINER_FEMALE | 
#line 253
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 254
        .doubleBattle = FALSE,
#line 255
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 257
            .species = SPECIES_PINECO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 259
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 258
            .lvl = 6,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 261
            .species = SPECIES_SWABLU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 263
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 262
            .lvl = 7,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 265
#line 267
    [DIFFICULTY_NORMAL][TRAINER_ROUTE3_KIM] =
    {
#line 266
        .trainerName = _("Kim"),
#line 268
        .trainerClass = TRAINER_CLASS_LASS,
#line 269
        .trainerPic = TRAINER_PIC_LASS,
        .encounterMusic_gender =
#line 270
F_TRAINER_FEMALE | 
#line 271
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 272
        .doubleBattle = FALSE,
#line 273
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 275
            .species = SPECIES_PINECO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 277
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 276
            .lvl = 6,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 278
            .species = SPECIES_SWABLU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 280
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 279
            .lvl = 7,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 283
#line 285
    [DIFFICULTY_EASY][TRAINER_ROUTE3_RONNIE] =
    {
#line 284
        .trainerName = _("Ronnie"),
#line 286
        .trainerClass = TRAINER_CLASS_BACKPACKER,
#line 287
        .trainerPic = TRAINER_PIC_BACKPACKER,
        .encounterMusic_gender =
#line 289
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 290
        .doubleBattle = FALSE,
#line 291
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 293
            .species = SPECIES_CUBONE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 295
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 294
            .lvl = 6,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 297
            .species = SPECIES_SENTRET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 299
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 298
            .lvl = 8,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 301
#line 303
    [DIFFICULTY_NORMAL][TRAINER_ROUTE3_RONNIE] =
    {
#line 302
        .trainerName = _("Ronnie"),
#line 304
        .trainerClass = TRAINER_CLASS_BACKPACKER,
#line 305
        .trainerPic = TRAINER_PIC_BACKPACKER,
        .encounterMusic_gender =
#line 307
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 308
        .doubleBattle = FALSE,
#line 309
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 311
            .species = SPECIES_CUBONE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 313
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 312
            .lvl = 6,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 314
            .species = SPECIES_SENTRET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 316
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 315
            .lvl = 8,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 318
#line 320
    [DIFFICULTY_EASY][TRAINER_ROUTE3_CHARA] =
    {
#line 319
        .trainerName = _("Chara"),
#line 321
        .trainerClass = TRAINER_CLASS_COOL_GIRL,
#line 322
        .trainerPic = TRAINER_PIC_COOL_GIRL,
        .encounterMusic_gender =
#line 323
F_TRAINER_FEMALE | 
#line 324
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 325
        .doubleBattle = FALSE,
#line 326
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 328
            .species = SPECIES_TEDDIURSA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 330
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 329
            .lvl = 7,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 332
            .species = SPECIES_SWABLU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 334
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 333
            .lvl = 9,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 337
    [DIFFICULTY_NORMAL][TRAINER_ROUTE3_CHARA] =
    {
#line 338
        .trainerName = _("Chara"),
#line 339
        .trainerClass = TRAINER_CLASS_COOL_GIRL,
#line 340
        .trainerPic = TRAINER_PIC_COOL_GIRL,
        .encounterMusic_gender =
#line 341
F_TRAINER_FEMALE | 
#line 342
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 343
        .doubleBattle = FALSE,
#line 344
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 346
            .species = SPECIES_TEDDIURSA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 348
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 347
            .lvl = 7,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 349
            .species = SPECIES_SWABLU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 351
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 350
            .lvl = 9,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 354
#line 356
    [DIFFICULTY_EASY][TRAINER_ROUTE3_EVIL_GABRIELLE] =
    {
#line 355
        .trainerName = _("Gabrielle"),
#line 357
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 358
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 359
F_TRAINER_FEMALE | 
#line 360
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 361
        .doubleBattle = FALSE,
#line 362
        .aiFlags = AI_FLAG_BASIC_TRAINER,
#line 363
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 365
            .species = SPECIES_ZORUA_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 367
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 366
            .lvl = 11,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 369
#line 371
    [DIFFICULTY_NORMAL][TRAINER_ROUTE3_EVIL_GABRIELLE] =
    {
#line 370
        .trainerName = _("Gabrielle"),
#line 372
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 373
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 374
F_TRAINER_FEMALE | 
#line 375
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 376
        .doubleBattle = FALSE,
#line 377
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
#line 378
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 380
            .species = SPECIES_ZORUA_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 382
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 381
            .lvl = 11,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 385
#line 387
    [DIFFICULTY_EASY][TRAINER_GASTREEGYM_JACO] =
    {
#line 386
        .trainerName = _("Jaco"),
#line 388
        .trainerClass = TRAINER_CLASS_YOUNGSTER,
#line 389
        .trainerPic = TRAINER_PIC_YOUNGSTER,
        .encounterMusic_gender =
#line 391
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 392
        .doubleBattle = FALSE,
#line 393
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 395
            .species = SPECIES_GEODUDE_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 397
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 396
            .lvl = 10,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 399
#line 401
    [DIFFICULTY_NORMAL][TRAINER_GASTREEGYM_JACO] =
    {
#line 400
        .trainerName = _("Jaco"),
#line 402
        .trainerClass = TRAINER_CLASS_YOUNGSTER,
#line 403
        .trainerPic = TRAINER_PIC_YOUNGSTER,
        .encounterMusic_gender =
#line 405
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 406
        .doubleBattle = FALSE,
#line 407
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 409
            .species = SPECIES_GEODUDE_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 411
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 410
            .lvl = 10,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 413
#line 415
    [DIFFICULTY_EASY][TRAINER_GASTREEGYM_SKIP] =
    {
#line 414
        .trainerName = _("Skip"),
#line 416
        .trainerClass = TRAINER_CLASS_BUILDER,
#line 417
        .trainerPic = TRAINER_PIC_BUILDER,
        .encounterMusic_gender =
#line 419
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 420
        .doubleBattle = FALSE,
#line 421
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 423
            .species = SPECIES_ROCKRUFF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 425
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 424
            .lvl = 10,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 427
            .species = SPECIES_GEODUDE_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 429
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 428
            .lvl = 11,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 431
#line 433
    [DIFFICULTY_NORMAL][TRAINER_GASTREEGYM_SKIP] =
    {
#line 432
        .trainerName = _("Skip"),
#line 434
        .trainerClass = TRAINER_CLASS_BUILDER,
#line 435
        .trainerPic = TRAINER_PIC_BUILDER,
        .encounterMusic_gender =
#line 437
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 438
        .doubleBattle = FALSE,
#line 439
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 441
            .species = SPECIES_ROCKRUFF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 443
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 442
            .lvl = 10,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 444
            .species = SPECIES_GEODUDE_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 446
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 445
            .lvl = 11,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 448
#line 450
    [DIFFICULTY_EASY][TRAINER_GASTREEGYM_LEADER] =
    {
#line 449
        .trainerName = _("Inger"),
#line 451
        .trainerClass = TRAINER_CLASS_LEADER,
#line 452
        .trainerPic = TRAINER_PIC_LEADER_INGER,
        .encounterMusic_gender =
#line 453
F_TRAINER_FEMALE | 
#line 454
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 457
        .items = { ITEM_POTION },
#line 455
        .doubleBattle = FALSE,
#line 456
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 458
        .mugshotColor = MUGSHOT_COLOR_YELLOW,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 460
            .species = SPECIES_ROCKRUFF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 462
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 461
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 463
                MOVE_SAND_ATTACK,
                MOVE_ROCK_THROW,
            },
            },
            {
#line 466
            .species = SPECIES_GEODUDE_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 468
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 467
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 470
            .species = SPECIES_MINIOR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 470
            .heldItem = ITEM_ORAN_BERRY,
#line 472
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 471
            .lvl = 13,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 473
                MOVE_CONFUSE_RAY,
                MOVE_ROLLOUT,
            },
            },
        },
    },
#line 476
#line 478
    [DIFFICULTY_NORMAL][TRAINER_GASTREEGYM_LEADER] =
    {
#line 477
        .trainerName = _("Inger"),
#line 479
        .trainerClass = TRAINER_CLASS_LEADER,
#line 480
        .trainerPic = TRAINER_PIC_LEADER_INGER,
        .encounterMusic_gender =
#line 481
F_TRAINER_FEMALE | 
#line 482
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 485
        .items = { ITEM_POTION },
#line 483
        .doubleBattle = FALSE,
#line 484
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 486
        .mugshotColor = MUGSHOT_COLOR_YELLOW,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 488
            .species = SPECIES_ROCKRUFF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 490
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 489
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 490
                MOVE_SAND_ATTACK,
                MOVE_ROCK_THROW,
            },
            },
            {
#line 493
            .species = SPECIES_GEODUDE_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 493
            .heldItem = ITEM_ORAN_BERRY,
#line 495
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 494
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 496
            .species = SPECIES_MINIOR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 496
            .heldItem = ITEM_ORAN_BERRY,
#line 497
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 498
            .lvl = 13,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 499
                MOVE_CONFUSE_RAY,
                MOVE_ROLLOUT,
            },
            },
        },
    },
#line 503
#line 505
    [DIFFICULTY_EASY][TRAINER_GASTREE_KOHLA] =
    {
#line 504
        .trainerName = _("Kohla"),
#line 506
        .trainerClass = TRAINER_CLASS_ACE_ROOKIE,
#line 507
        .trainerPic = TRAINER_PIC_WALLY,
        .encounterMusic_gender =
#line 509
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 510
        .doubleBattle = FALSE,
#line 511
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 513
            .species = SPECIES_YAMPER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 515
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 514
            .lvl = 11,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 517
            .species = SPECIES_CHARCADET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 519
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 518
            .lvl = 13,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 521
#line 523
    [DIFFICULTY_NORMAL][TRAINER_GASTREE_KOHLA] =
    {
#line 522
        .trainerName = _("Kohla"),
#line 524
        .trainerClass = TRAINER_CLASS_ACE_ROOKIE,
#line 525
        .trainerPic = TRAINER_PIC_WALLY,
        .encounterMusic_gender =
#line 527
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 528
        .doubleBattle = FALSE,
#line 529
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 531
            .species = SPECIES_YAMPER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 533
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 532
            .lvl = 11,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 534
            .species = SPECIES_CHARCADET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 534
            .heldItem = ITEM_ORAN_BERRY,
#line 536
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 535
            .lvl = 13,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 540
#line 542
    [DIFFICULTY_EASY][TRAINER_ROUTE4_GRUNTS] =
    {
#line 541
        .trainerName = _("Duo"),
#line 543
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 544
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_DUO,
        .encounterMusic_gender =
#line 546
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 547
        .doubleBattle = TRUE,
#line 548
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 550
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 552
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 551
            .lvl = 13,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 554
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 556
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 555
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 558
#line 560
    [DIFFICULTY_NORMAL][TRAINER_ROUTE4_GRUNTS] =
    {
#line 559
        .trainerName = _("Duo"),
#line 561
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 562
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_DUO,
        .encounterMusic_gender =
#line 564
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 565
        .doubleBattle = TRUE,
#line 566
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 568
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 570
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 569
            .lvl = 13,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 571
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 573
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 572
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 582
#line 584
    [DIFFICULTY_EASY][TRAINER_CERAMBASECAMP_EVIL_GABRIELLE] =
    {
#line 583
        .trainerName = _("Gabrielle"),
#line 585
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 586
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 587
F_TRAINER_FEMALE | 
#line 588
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 589
        .doubleBattle = FALSE,
#line 590
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
#line 591
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 593
            .species = SPECIES_ZORUA_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 595
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 594
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 596
            .species = SPECIES_BALTOY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 598
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 597
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 599
#line 601
    [DIFFICULTY_NORMAL][TRAINER_CERAMBASECAMP_EVIL_GABRIELLE] =
    {
#line 600
        .trainerName = _("Gabrielle"),
#line 602
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 603
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 604
F_TRAINER_FEMALE | 
#line 605
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 606
        .doubleBattle = FALSE,
#line 607
        .aiFlags = AI_FLAG_SMART_TRAINER,
#line 608
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 610
            .species = SPECIES_ZORUA_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 610
            .heldItem = ITEM_GHOST_GEM,
#line 612
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 611
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 613
            .species = SPECIES_BALTOY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 615
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 614
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 624
#line 626
    [DIFFICULTY_EASY][TRAINER_CERAMBASECAMP_GRUNT1] =
    {
#line 625
        .trainerName = _("Grunt"),
#line 627
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 628
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 630
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 631
        .doubleBattle = FALSE,
#line 632
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 634
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 636
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 635
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 638
#line 640
    [DIFFICULTY_NORMAL][TRAINER_CERAMBASECAMP_GRUNT1] =
    {
#line 639
        .trainerName = _("Grunt"),
#line 641
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 642
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 644
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 645
        .doubleBattle = FALSE,
#line 646
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 648
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 650
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 649
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 661
#line 663
    [DIFFICULTY_EASY][TRAINER_CERAMBASECAMP_GRUNT2] =
    {
#line 662
        .trainerName = _("Grunt"),
#line 664
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 665
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 667
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 668
        .doubleBattle = FALSE,
#line 669
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 671
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 673
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 672
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 675
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 677
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 676
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 679
#line 681
    [DIFFICULTY_NORMAL][TRAINER_CERAMBASECAMP_GRUNT2] =
    {
#line 680
        .trainerName = _("Grunt"),
#line 682
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 683
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 685
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 686
        .doubleBattle = FALSE,
#line 687
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 689
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 691
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 690
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 692
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 694
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 693
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 705
#line 707
    [DIFFICULTY_EASY][TRAINER_CERAMBASECAMP_GRUNT3] =
    {
#line 706
        .trainerName = _("Grunt"),
#line 708
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 709
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 711
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 712
        .doubleBattle = FALSE,
#line 713
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 715
            .species = SPECIES_BRONZOR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 717
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 716
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 719
            .species = SPECIES_YANMA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 721
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 720
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 723
#line 725
    [DIFFICULTY_NORMAL][TRAINER_CERAMBASECAMP_GRUNT3] =
    {
#line 724
        .trainerName = _("Grunt"),
#line 726
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 727
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 729
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 730
        .doubleBattle = FALSE,
#line 731
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 733
            .species = SPECIES_BRONZOR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 735
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 734
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 736
            .species = SPECIES_YANMA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 738
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 737
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 750
#line 752
    [DIFFICULTY_EASY][TRAINER_ROUTE4_RAHA] =
    {
#line 751
        .trainerName = _("Raha"),
#line 753
        .trainerClass = TRAINER_CLASS_RICH_BOY,
#line 754
        .trainerPic = TRAINER_PIC_RICH_BOY,
        .encounterMusic_gender =
#line 756
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 757
        .doubleBattle = FALSE,
#line 758
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 760
            .species = SPECIES_CHINCHOU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 763
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 762
            .lvl = 13,
            .nature = NATURE_HARDY,
#line 761
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 766
#line 768
    [DIFFICULTY_NORMAL][TRAINER_ROUTE4_RAHA] =
    {
#line 767
        .trainerName = _("Raha"),
#line 769
        .trainerClass = TRAINER_CLASS_RICH_BOY,
#line 770
        .trainerPic = TRAINER_PIC_RICH_BOY,
        .encounterMusic_gender =
#line 772
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 773
        .doubleBattle = FALSE,
#line 774
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 776
            .species = SPECIES_CHINCHOU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 779
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 778
            .lvl = 13,
            .nature = NATURE_HARDY,
#line 777
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 781
#line 783
    [DIFFICULTY_EASY][TRAINER_ROUTE4_CAMMY] =
    {
#line 782
        .trainerName = _("Cammy"),
#line 784
        .trainerClass = TRAINER_CLASS_EXPERT,
#line 785
        .trainerPic = TRAINER_PIC_EXPERT_F,
        .encounterMusic_gender =
#line 786
F_TRAINER_FEMALE | 
#line 787
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 788
        .doubleBattle = FALSE,
#line 789
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 791
            .species = SPECIES_GREAVARD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 793
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 792
            .lvl = 9,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 795
            .species = SPECIES_SWABLU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 797
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 796
            .lvl = 10,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 799
#line 801
    [DIFFICULTY_NORMAL][TRAINER_ROUTE4_CAMMY] =
    {
#line 800
        .trainerName = _("Cammy"),
#line 802
        .trainerClass = TRAINER_CLASS_EXPERT,
#line 803
        .trainerPic = TRAINER_PIC_EXPERT_F,
        .encounterMusic_gender =
#line 804
F_TRAINER_FEMALE | 
#line 805
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 806
        .doubleBattle = FALSE,
#line 807
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 809
            .species = SPECIES_SWABLU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 811
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 810
            .lvl = 9,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 812
            .species = SPECIES_GREAVARD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 814
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 813
            .lvl = 10,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 816
#line 818
    [DIFFICULTY_EASY][TRAINER_ROUTE4_SONA] =
    {
#line 817
        .trainerName = _("Sona"),
#line 819
        .trainerClass = TRAINER_CLASS_LASS,
#line 820
        .trainerPic = TRAINER_PIC_LASS,
        .encounterMusic_gender =
#line 821
F_TRAINER_FEMALE | 
#line 822
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 823
        .doubleBattle = FALSE,
#line 824
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 826
            .species = SPECIES_BUNEARY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 828
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 827
            .lvl = 11,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 830
            .species = SPECIES_CHIKORITA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 832
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 831
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 835
#line 837
    [DIFFICULTY_NORMAL][TRAINER_ROUTE4_SONA] =
    {
#line 836
        .trainerName = _("Sona"),
#line 838
        .trainerClass = TRAINER_CLASS_LASS,
#line 839
        .trainerPic = TRAINER_PIC_LASS,
        .encounterMusic_gender =
#line 840
F_TRAINER_FEMALE | 
#line 841
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 842
        .doubleBattle = FALSE,
#line 843
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 845
            .species = SPECIES_BUNEARY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 847
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 846
            .lvl = 11,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 848
            .species = SPECIES_CHIKORITA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 850
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 849
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 852
#line 854
    [DIFFICULTY_EASY][TRAINER_ROUTE4_JENNY] =
    {
#line 853
        .trainerName = _("Jenny"),
#line 855
        .trainerClass = TRAINER_CLASS_LASS,
#line 856
        .trainerPic = TRAINER_PIC_LASS,
        .encounterMusic_gender =
#line 857
F_TRAINER_FEMALE | 
#line 858
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 859
        .doubleBattle = FALSE,
#line 860
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 862
            .species = SPECIES_BUNEARY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 864
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 863
            .lvl = 11,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 866
            .species = SPECIES_CHIKORITA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 868
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 867
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 870
#line 872
    [DIFFICULTY_NORMAL][TRAINER_ROUTE4_JENNY] =
    {
#line 871
        .trainerName = _("Jenny"),
#line 873
        .trainerClass = TRAINER_CLASS_LASS,
#line 874
        .trainerPic = TRAINER_PIC_LASS,
        .encounterMusic_gender =
#line 875
F_TRAINER_FEMALE | 
#line 876
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 877
        .doubleBattle = FALSE,
#line 878
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 880
            .species = SPECIES_BUNEARY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 882
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 881
            .lvl = 11,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 883
            .species = SPECIES_CHIKORITA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 885
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 884
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 887
#line 889
    [DIFFICULTY_EASY][TRAINER_ROUTE4_KID1] =
    {
#line 888
        .trainerName = _("Morty"),
#line 890
        .trainerClass = TRAINER_CLASS_NINJA_BOY,
#line 891
        .trainerPic = TRAINER_PIC_NINJA_BOY,
        .encounterMusic_gender =
#line 893
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 894
        .doubleBattle = FALSE,
#line 895
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE | AI_FLAG_TRY_TO_FAINT,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 897
            .species = SPECIES_PIDOVE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 899
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 898
            .lvl = 11,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 901
#line 903
    [DIFFICULTY_NORMAL][TRAINER_ROUTE4_KID1] =
    {
#line 902
        .trainerName = _("Morty"),
#line 904
        .trainerClass = TRAINER_CLASS_NINJA_BOY,
#line 905
        .trainerPic = TRAINER_PIC_NINJA_BOY,
        .encounterMusic_gender =
#line 907
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 908
        .doubleBattle = FALSE,
#line 909
        .aiFlags = AI_FLAG_BASIC_TRAINER | AI_FLAG_TRY_TO_FAINT,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 911
            .species = SPECIES_PIDOVE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 913
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 912
            .lvl = 11,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 921
#line 923
    [DIFFICULTY_EASY][TRAINER_ROUTE4_KID2] =
    {
#line 922
        .trainerName = _("Lala"),
#line 924
        .trainerClass = TRAINER_CLASS_PICNICKER,
#line 925
        .trainerPic = TRAINER_PIC_PICNICKER,
        .encounterMusic_gender =
#line 926
F_TRAINER_FEMALE | 
#line 927
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 928
        .doubleBattle = FALSE,
#line 929
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 931
            .species = SPECIES_BUDEW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 933
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 932
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 935
#line 937
    [DIFFICULTY_NORMAL][TRAINER_ROUTE4_KID2] =
    {
#line 936
        .trainerName = _("Lala"),
#line 938
        .trainerClass = TRAINER_CLASS_PICNICKER,
#line 939
        .trainerPic = TRAINER_PIC_PICNICKER,
        .encounterMusic_gender =
#line 940
F_TRAINER_FEMALE | 
#line 941
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 942
        .doubleBattle = FALSE,
#line 943
        .aiFlags = AI_FLAG_BASIC_TRAINER | AI_FLAG_TRY_TO_FAINT,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 945
            .species = SPECIES_BUDEW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 947
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 946
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 950
#line 952
    [DIFFICULTY_EASY][TRAINER_ROUTE4_KID3] =
    {
#line 951
        .trainerName = _("Pine"),
#line 953
        .trainerClass = TRAINER_CLASS_SCHOOL_KID,
#line 954
        .trainerPic = TRAINER_PIC_SCHOOL_KID_M,
        .encounterMusic_gender =
#line 956
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 957
        .doubleBattle = FALSE,
#line 958
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 959
        .mugshotColor = MUGSHOT_COLOR_BLUE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 961
            .species = SPECIES_TOGEPI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 963
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 962
            .lvl = 13,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 965
            .species = SPECIES_MIME_JR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 967
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 966
            .lvl = 13,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 969
#line 971
    [DIFFICULTY_NORMAL][TRAINER_ROUTE4_KID3] =
    {
#line 970
        .trainerName = _("Pine"),
#line 972
        .trainerClass = TRAINER_CLASS_SCHOOL_KID,
#line 973
        .trainerPic = TRAINER_PIC_SCHOOL_KID_M,
        .encounterMusic_gender =
#line 975
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 976
        .doubleBattle = FALSE,
#line 977
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 978
        .mugshotColor = MUGSHOT_COLOR_BLUE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 980
            .species = SPECIES_TOGEPI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 982
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 981
            .lvl = 13,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 983
            .species = SPECIES_MIME_JR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 985
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 984
            .lvl = 13,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 989
#line 991
    [DIFFICULTY_EASY][TRAINER_CERAMBASECAMPGYM_A] =
    {
#line 990
        .trainerName = _("Tanner"),
#line 992
        .trainerClass = TRAINER_CLASS_EMPLOYEE,
#line 993
        .trainerPic = TRAINER_PIC_EMPLOYEE,
        .encounterMusic_gender =
#line 995
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 996
        .doubleBattle = FALSE,
#line 997
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 999
            .species = SPECIES_ROLYCOLY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1001
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1000
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1003
#line 1005
    [DIFFICULTY_NORMAL][TRAINER_CERAMBASECAMPGYM_A] =
    {
#line 1004
        .trainerName = _("Tanner"),
#line 1006
        .trainerClass = TRAINER_CLASS_EMPLOYEE,
#line 1007
        .trainerPic = TRAINER_PIC_EMPLOYEE,
        .encounterMusic_gender =
#line 1009
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 1010
        .doubleBattle = FALSE,
#line 1011
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 1013
            .species = SPECIES_ROLYCOLY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1015
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1014
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1017
#line 1019
    [DIFFICULTY_EASY][TRAINER_CERAMBASECAMPGYM_B] =
    {
#line 1018
        .trainerName = _("Bron"),
#line 1020
        .trainerClass = TRAINER_CLASS_KINDLER,
#line 1021
        .trainerPic = TRAINER_PIC_KINDLER,
        .encounterMusic_gender =
#line 1023
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 1024
        .doubleBattle = FALSE,
#line 1025
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1027
            .species = SPECIES_ROLYCOLY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1029
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1028
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1031
            .species = SPECIES_FLETCHLING,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1033
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1032
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1036
#line 1038
    [DIFFICULTY_NORMAL][TRAINER_CERAMBASECAMPGYM_B] =
    {
#line 1037
        .trainerName = _("Bron"),
#line 1039
        .trainerClass = TRAINER_CLASS_KINDLER,
#line 1040
        .trainerPic = TRAINER_PIC_KINDLER,
        .encounterMusic_gender =
#line 1042
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 1043
        .doubleBattle = FALSE,
#line 1044
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1046
            .species = SPECIES_ROLYCOLY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1048
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1047
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1049
            .species = SPECIES_FLETCHLING,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1051
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1050
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1053
#line 1055
    [DIFFICULTY_EASY][TRAINER_CERAMBASECAMPGYM_C] =
    {
#line 1054
        .trainerName = _("Jordi"),
#line 1056
        .trainerClass = TRAINER_CLASS_EMPLOYEE,
#line 1057
        .trainerPic = TRAINER_PIC_EMPLOYEE,
        .encounterMusic_gender =
#line 1059
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 1060
        .doubleBattle = FALSE,
#line 1061
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 1063
            .species = SPECIES_BRAIXEN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1065
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1064
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1067
#line 1069
    [DIFFICULTY_NORMAL][TRAINER_CERAMBASECAMPGYM_C] =
    {
#line 1068
        .trainerName = _("Jordi"),
#line 1070
        .trainerClass = TRAINER_CLASS_EMPLOYEE,
#line 1071
        .trainerPic = TRAINER_PIC_EMPLOYEE,
        .encounterMusic_gender =
#line 1073
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 1074
        .doubleBattle = FALSE,
#line 1075
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_TRY_TO_FAINT,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 1077
            .species = SPECIES_BRAIXEN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1079
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1078
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1082
#line 1084
    [DIFFICULTY_EASY][TRAINER_CERAMBASECAMPGYM_D] =
    {
#line 1083
        .trainerName = _("Alba"),
#line 1085
        .trainerClass = TRAINER_CLASS_EMPLOYEE,
#line 1086
        .trainerPic = TRAINER_PIC_EMPLOYEE,
        .encounterMusic_gender =
#line 1088
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 1089
        .doubleBattle = FALSE,
#line 1090
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1092
            .species = SPECIES_FLETCHLING,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1094
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 1093
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1096
            .species = SPECIES_SIZZLIPEDE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1098
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 1097
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1102
#line 1104
    [DIFFICULTY_NORMAL][TRAINER_CERAMBASECAMPGYM_D] =
    {
#line 1103
        .trainerName = _("Alba"),
#line 1105
        .trainerClass = TRAINER_CLASS_EMPLOYEE,
#line 1106
        .trainerPic = TRAINER_PIC_EMPLOYEE,
        .encounterMusic_gender =
#line 1108
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 1109
        .doubleBattle = FALSE,
#line 1110
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1112
            .species = SPECIES_FLETCHLING,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1114
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1113
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1115
            .species = SPECIES_SIZZLIPEDE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1117
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1116
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1128
#line 1130
    [DIFFICULTY_EASY][TRAINER_CERAMBASECAMPGYM_LEADER] =
    {
#line 1129
        .trainerName = _("Ariana"),
#line 1131
        .trainerClass = TRAINER_CLASS_LEADER,
#line 1132
        .trainerPic = TRAINER_PIC_LEADER_ARIANA,
        .encounterMusic_gender =
#line 1134
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 1135
        .items = { ITEM_SUPER_POTION },
#line 1136
        .doubleBattle = FALSE,
#line 1137
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 1138
        .mugshotColor = MUGSHOT_COLOR_PINK,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 1140
            .species = SPECIES_GROWLITHE_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1143
            .iv = TRAINER_PARTY_IVS(6, 6, 6, 6, 6, 6),
#line 1141
            .ability = ABILITY_INTIMIDATE,
#line 1142
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 1144
                MOVE_FLAME_WHEEL,
                MOVE_BITE,
                MOVE_ROCK_TOMB,
                MOVE_ROAR,
            },
            },
            {
#line 1149
            .species = SPECIES_SIZZLIPEDE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1151
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 1150
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1153
            .species = SPECIES_TAUROS_PALDEA_BLAZE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1156
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 1154
            .ability = ABILITY_INTIMIDATE,
#line 1155
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1158
#line 1160
    [DIFFICULTY_NORMAL][TRAINER_CERAMBASECAMPGYM_LEADER] =
    {
#line 1159
        .trainerName = _("Ariana"),
#line 1161
        .trainerClass = TRAINER_CLASS_LEADER,
#line 1162
        .trainerPic = TRAINER_PIC_LEADER_ARIANA,
        .encounterMusic_gender =
#line 1164
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 1165
        .items = { ITEM_SUPER_POTION },
#line 1166
        .doubleBattle = FALSE,
#line 1167
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 1168
        .mugshotColor = MUGSHOT_COLOR_PINK,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 1170
            .species = SPECIES_GROWLITHE_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1170
            .heldItem = ITEM_ORAN_BERRY,
#line 1173
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1171
            .ability = ABILITY_INTIMIDATE,
#line 1172
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 1173
                MOVE_FLAME_WHEEL,
                MOVE_BITE,
                MOVE_ROCK_TOMB,
                MOVE_ROAR,
            },
            },
            {
#line 1178
            .species = SPECIES_SIZZLIPEDE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1178
            .heldItem = ITEM_FOCUS_SASH,
#line 1180
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1179
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1181
            .species = SPECIES_TAUROS_PALDEA_BLAZE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1181
            .heldItem = ITEM_ORAN_BERRY,
#line 1184
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1182
            .ability = ABILITY_INTIMIDATE,
#line 1183
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1195
#line 1197
    [DIFFICULTY_EASY][TRAINER_MTCERAM_A] =
    {
#line 1196
        .trainerName = _("Xander"),
#line 1198
        .trainerClass = TRAINER_CLASS_BLACK_BELT,
#line 1199
        .trainerPic = TRAINER_PIC_BLACK_BELT,
        .encounterMusic_gender =
#line 1201
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 1202
        .doubleBattle = FALSE,
#line 1203
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1205
            .species = SPECIES_SNEASEL_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1207
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1206
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1209
            .species = SPECIES_MANKEY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1211
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1210
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1213
#line 1215
    [DIFFICULTY_NORMAL][TRAINER_MTCERAM_A] =
    {
#line 1214
        .trainerName = _("Xander"),
#line 1216
        .trainerClass = TRAINER_CLASS_BLACK_BELT,
#line 1217
        .trainerPic = TRAINER_PIC_BLACK_BELT,
        .encounterMusic_gender =
#line 1219
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 1220
        .doubleBattle = FALSE,
#line 1221
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1223
            .species = SPECIES_SNEASEL_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1225
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1224
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1226
            .species = SPECIES_MANKEY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1228
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1227
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1230
#line 1232
    [DIFFICULTY_EASY][TRAINER_MTCERAM_B] =
    {
#line 1231
        .trainerName = _("Edsun"),
#line 1233
        .trainerClass = TRAINER_CLASS_FIREFIGHTER,
#line 1234
        .trainerPic = TRAINER_PIC_FIREFIGHTER,
        .encounterMusic_gender =
#line 1236
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 1237
        .doubleBattle = FALSE,
#line 1238
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1240
            .species = SPECIES_FINNEON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1242
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1241
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1244
            .species = SPECIES_TOTODILE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1246
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1245
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1250
#line 1252
    [DIFFICULTY_NORMAL][TRAINER_MTCERAM_B] =
    {
#line 1251
        .trainerName = _("Edsun"),
#line 1253
        .trainerClass = TRAINER_CLASS_FIREFIGHTER,
#line 1254
        .trainerPic = TRAINER_PIC_FIREFIGHTER,
        .encounterMusic_gender =
#line 1256
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 1257
        .doubleBattle = FALSE,
#line 1258
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1260
            .species = SPECIES_FINNEON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1262
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1261
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1263
            .species = SPECIES_TOTODILE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1265
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1264
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1268
#line 1270
    [DIFFICULTY_EASY][TRAINER_MTCERAM_C] =
    {
#line 1269
        .trainerName = _("Hayden"),
#line 1271
        .trainerClass = TRAINER_CLASS_KINDLER,
#line 1272
        .trainerPic = TRAINER_PIC_KINDLER,
        .encounterMusic_gender =
#line 1274
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 1275
        .doubleBattle = FALSE,
#line 1276
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1278
            .species = SPECIES_FLETCHLING,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1280
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1279
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1282
            .species = SPECIES_SIZZLIPEDE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1284
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1283
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1287
#line 1289
    [DIFFICULTY_NORMAL][TRAINER_MTCERAM_C] =
    {
#line 1288
        .trainerName = _("Hayden"),
#line 1290
        .trainerClass = TRAINER_CLASS_KINDLER,
#line 1291
        .trainerPic = TRAINER_PIC_KINDLER,
        .encounterMusic_gender =
#line 1293
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 1294
        .doubleBattle = FALSE,
#line 1295
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1297
            .species = SPECIES_FLETCHLING,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1299
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1298
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1300
            .species = SPECIES_SIZZLIPEDE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1302
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1301
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1305
#line 1307
    [DIFFICULTY_EASY][TRAINER_MTCERAM_D] =
    {
#line 1306
        .trainerName = _("Janet"),
#line 1308
        .trainerClass = TRAINER_CLASS_PKMN_BREEDER,
#line 1309
        .trainerPic = TRAINER_PIC_POKEMON_BREEDER_F,
        .encounterMusic_gender =
#line 1310
F_TRAINER_FEMALE | 
#line 1311
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1312
        .doubleBattle = FALSE,
#line 1313
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1315
            .species = SPECIES_MAREEP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1317
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1316
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1319
            .species = SPECIES_WOOLOO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1321
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1320
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1323
#line 1325
    [DIFFICULTY_NORMAL][TRAINER_MTCERAM_D] =
    {
#line 1324
        .trainerName = _("Janet"),
#line 1326
        .trainerClass = TRAINER_CLASS_PKMN_BREEDER,
#line 1327
        .trainerPic = TRAINER_PIC_POKEMON_BREEDER_F,
        .encounterMusic_gender =
#line 1328
F_TRAINER_FEMALE | 
#line 1329
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1330
        .doubleBattle = FALSE,
#line 1331
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1333
            .species = SPECIES_MAREEP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1335
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1334
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1336
            .species = SPECIES_WOOLOO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1338
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1337
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1342
#line 1344
    [DIFFICULTY_EASY][TRAINER_MTCERAM_GRUNT1] =
    {
#line 1343
        .trainerName = _("Grunt"),
#line 1345
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 1346
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 1348
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 1349
        .doubleBattle = FALSE,
#line 1350
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 1352
            .species = SPECIES_YANMA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1354
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1353
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1356
#line 1358
    [DIFFICULTY_NORMAL][TRAINER_MTCERAM_GRUNT1] =
    {
#line 1357
        .trainerName = _("Grunt"),
#line 1359
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 1360
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 1362
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 1363
        .doubleBattle = FALSE,
#line 1364
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 1366
            .species = SPECIES_YANMA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1366
            .heldItem = ITEM_CHARTI_BERRY,
#line 1368
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1367
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1370
#line 1372
    [DIFFICULTY_EASY][TRAINER_MTCERAM_GRUNT2] =
    {
#line 1371
        .trainerName = _("Grunt"),
#line 1373
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 1374
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 1376
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 1377
        .doubleBattle = FALSE,
#line 1378
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1380
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1382
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1381
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1384
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1386
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1385
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1388
#line 1390
    [DIFFICULTY_NORMAL][TRAINER_MTCERAM_GRUNT2] =
    {
#line 1389
        .trainerName = _("Grunt"),
#line 1391
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 1392
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 1394
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 1395
        .doubleBattle = FALSE,
#line 1396
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1398
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1400
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1399
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1401
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1403
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1402
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1409
#line 1411
    [DIFFICULTY_EASY][TRAINER_MTCERAM_GRUNT_DOUBLE] =
    {
#line 1410
        .trainerName = _("Duo"),
#line 1412
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 1413
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_DUO,
        .encounterMusic_gender =
#line 1414
F_TRAINER_FEMALE | 
#line 1415
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1416
        .doubleBattle = TRUE,
#line 1417
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 1419
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1421
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1420
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1423
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1425
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1424
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1427
            .species = SPECIES_YANMA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1429
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1428
            .lvl = 18,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1431
            .species = SPECIES_BRONZOR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1433
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1432
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1437
#line 1439
    [DIFFICULTY_NORMAL][TRAINER_MTCERAM_GRUNT_DOUBLE] =
    {
#line 1438
        .trainerName = _("Duo"),
#line 1440
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 1441
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_DUO,
        .encounterMusic_gender =
#line 1442
F_TRAINER_FEMALE | 
#line 1443
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1444
        .doubleBattle = TRUE,
#line 1445
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 1447
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1449
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1448
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1450
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1452
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1451
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1453
            .species = SPECIES_YANMA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1455
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1454
            .lvl = 18,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1456
            .species = SPECIES_BRONZOR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1456
            .heldItem = ITEM_ORAN_BERRY,
#line 1458
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1457
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1461
#line 1463
    [DIFFICULTY_EASY][TRAINER_CERAMPEAK_MOXIE] =
    {
#line 1462
        .trainerName = _("Moxie"),
#line 1464
        .trainerClass = TRAINER_CLASS_SOMBER_ADMIN,
#line 1465
        .trainerPic = TRAINER_PIC_SOMBER_ADMIN_MOXIE,
        .encounterMusic_gender =
#line 1467
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 1468
        .items = { ITEM_SUPER_POTION },
#line 1469
        .doubleBattle = FALSE,
#line 1470
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 1471
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 1473
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1475
            .iv = TRAINER_PARTY_IVS(5, 5, 5, 5, 5, 5),
#line 1474
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1477
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1479
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1478
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1480
            .species = SPECIES_SLOWPOKE_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1482
            .iv = TRAINER_PARTY_IVS(5, 5, 5, 5, 5, 5),
#line 1481
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 1483
                MOVE_ACID,
                MOVE_YAWN,
                MOVE_PSYCHIC,
                MOVE_WATER_PULSE,
            },
            },
        },
    },
#line 1489
#line 1491
    [DIFFICULTY_NORMAL][TRAINER_CERAMPEAK_MOXIE] =
    {
#line 1490
        .trainerName = _("Moxie"),
#line 1492
        .trainerClass = TRAINER_CLASS_SOMBER_ADMIN,
#line 1493
        .trainerPic = TRAINER_PIC_SOMBER_ADMIN_MOXIE,
        .encounterMusic_gender =
#line 1495
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 1496
        .items = { ITEM_SUPER_POTION },
#line 1497
        .doubleBattle = FALSE,
#line 1498
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 1499
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 1501
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1503
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1502
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1504
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1504
            .heldItem = ITEM_ORAN_BERRY,
#line 1506
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1505
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1507
            .species = SPECIES_SLOWPOKE_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1509
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1508
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 1509
                MOVE_ACID,
                MOVE_YAWN,
                MOVE_PSYCHIC,
                MOVE_WATER_PULSE,
            },
            },
        },
    },
#line 1526
#line 1528
    [DIFFICULTY_EASY][TRAINER_GALECREST_ROBBER] =
    {
#line 1527
        .trainerName = _("Xander"),
#line 1529
        .trainerClass = TRAINER_CLASS_BURGLAR,
#line 1530
        .trainerPic = TRAINER_PIC_BURGLAR,
        .encounterMusic_gender =
#line 1531
F_TRAINER_FEMALE | 
#line 1532
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1533
        .doubleBattle = FALSE,
#line 1534
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1536
            .species = SPECIES_NICKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1538
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1537
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1540
            .species = SPECIES_RATTATA_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1542
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1541
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1545
#line 1547
    [DIFFICULTY_NORMAL][TRAINER_GALECREST_ROBBER] =
    {
#line 1546
        .trainerName = _("Xander"),
#line 1548
        .trainerClass = TRAINER_CLASS_BURGLAR,
#line 1549
        .trainerPic = TRAINER_PIC_BURGLAR,
        .encounterMusic_gender =
#line 1550
F_TRAINER_FEMALE | 
#line 1551
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1552
        .doubleBattle = FALSE,
#line 1553
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1555
            .species = SPECIES_NICKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1557
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1556
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1558
            .species = SPECIES_RATICATE_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1560
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1559
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1562
#line 1564
    [DIFFICULTY_EASY][TRAINER_GALECREST_DETECTIVE_A] =
    {
#line 1563
        .trainerName = _("Candy"),
#line 1565
        .trainerClass = TRAINER_CLASS_CADET,
#line 1566
        .trainerPic = TRAINER_PIC_CADET_F,
        .encounterMusic_gender =
#line 1567
F_TRAINER_FEMALE | 
#line 1568
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1569
        .doubleBattle = FALSE,
#line 1570
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 1572
            .species = SPECIES_CHARCADET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1574
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 1573
            .lvl = 18,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1576
#line 1578
    [DIFFICULTY_NORMAL][TRAINER_GALECREST_DETECTIVE_A] =
    {
#line 1577
        .trainerName = _("Candy"),
#line 1579
        .trainerClass = TRAINER_CLASS_CADET,
#line 1580
        .trainerPic = TRAINER_PIC_CADET_F,
        .encounterMusic_gender =
#line 1581
F_TRAINER_FEMALE | 
#line 1582
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1583
        .doubleBattle = FALSE,
#line 1584
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 1586
            .species = SPECIES_CHARCADET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1588
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1587
            .lvl = 18,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1591
#line 1593
    [DIFFICULTY_EASY][TRAINER_GALECREST_B] =
    {
#line 1592
        .trainerName = _("Evio"),
#line 1594
        .trainerClass = TRAINER_CLASS_RUIN_MANIAC,
#line 1595
        .trainerPic = TRAINER_PIC_RUIN_MANIAC,
        .encounterMusic_gender =
#line 1597
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 1598
        .doubleBattle = FALSE,
#line 1599
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 1601
            .species = SPECIES_SHROOMISH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1603
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 1602
            .lvl = 10,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1605
            .species = SPECIES_GLOOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1607
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 1606
            .lvl = 10,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1609
            .species = SPECIES_ROSELIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1611
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 1610
            .lvl = 10,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1614
#line 1616
    [DIFFICULTY_EASY][TRAINER_GALECRESTGYM_A] =
    {
#line 1615
        .trainerName = _("Ronnie"),
#line 1617
        .trainerClass = TRAINER_CLASS_CADET,
#line 1618
        .trainerPic = TRAINER_PIC_CADET_M,
        .encounterMusic_gender =
#line 1620
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 1621
        .doubleBattle = FALSE,
#line 1622
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1624
            .species = SPECIES_CHARCADET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1626
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 1625
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1628
            .species = SPECIES_FURFROU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1630
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 1629
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 1631
                MOVE_HEADBUTT,
                MOVE_SNARL,
                MOVE_GROWL,
            },
            },
        },
    },
#line 1635
#line 1637
    [DIFFICULTY_NORMAL][TRAINER_GALECRESTGYM_A] =
    {
#line 1636
        .trainerName = _("Ronnie"),
#line 1638
        .trainerClass = TRAINER_CLASS_CADET,
#line 1639
        .trainerPic = TRAINER_PIC_CADET_M,
        .encounterMusic_gender =
#line 1641
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 1642
        .doubleBattle = FALSE,
#line 1643
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1645
            .species = SPECIES_CHARCADET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1647
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1646
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1648
            .species = SPECIES_FURFROU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1650
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1649
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 1650
                MOVE_HEADBUTT,
                MOVE_SNARL,
                MOVE_GROWL,
            },
            },
        },
    },
#line 1657
#line 1659
    [DIFFICULTY_EASY][TRAINER_GALECRESTGYM_B] =
    {
#line 1658
        .trainerName = _("Rose"),
#line 1660
        .trainerClass = TRAINER_CLASS_CADET,
#line 1661
        .trainerPic = TRAINER_PIC_CADET_F,
        .encounterMusic_gender =
#line 1662
F_TRAINER_FEMALE | 
#line 1663
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1664
        .doubleBattle = FALSE,
#line 1665
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 1667
            .species = SPECIES_HERDIER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1669
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 1668
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1671
            .species = SPECIES_TRANQUILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1673
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 1672
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1675
            .species = SPECIES_CHARCADET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1677
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 1676
            .lvl = 18,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1679
#line 1681
    [DIFFICULTY_NORMAL][TRAINER_GALECRESTGYM_B] =
    {
#line 1680
        .trainerName = _("Rose"),
#line 1682
        .trainerClass = TRAINER_CLASS_CADET,
#line 1683
        .trainerPic = TRAINER_PIC_CADET_F,
        .encounterMusic_gender =
#line 1684
F_TRAINER_FEMALE | 
#line 1685
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1686
        .doubleBattle = FALSE,
#line 1687
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 1689
            .species = SPECIES_HERDIER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1691
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1690
            .lvl = 16,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1692
            .species = SPECIES_TRANQUILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1694
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1693
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1695
            .species = SPECIES_CHARCADET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1697
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1696
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1702
#line 1704
    [DIFFICULTY_EASY][TRAINER_GALECRESTGYM_C] =
    {
#line 1703
        .trainerName = _("Bonnie"),
#line 1705
        .trainerClass = TRAINER_CLASS_CADET,
#line 1706
        .trainerPic = TRAINER_PIC_CADET_F,
        .encounterMusic_gender =
#line 1707
F_TRAINER_FEMALE | 
#line 1708
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1709
        .doubleBattle = FALSE,
#line 1710
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1712
            .species = SPECIES_CHARCADET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1714
            .iv = TRAINER_PARTY_IVS(6, 6, 6, 6, 6, 6),
#line 1713
            .lvl = 18,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1716
            .species = SPECIES_SENTRET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1718
            .iv = TRAINER_PARTY_IVS(6, 6, 6, 6, 6, 6),
#line 1717
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1720
#line 1722
    [DIFFICULTY_NORMAL][TRAINER_GALECRESTGYM_C] =
    {
#line 1721
        .trainerName = _("Bonnie"),
#line 1723
        .trainerClass = TRAINER_CLASS_CADET,
#line 1724
        .trainerPic = TRAINER_PIC_CADET_F,
        .encounterMusic_gender =
#line 1725
F_TRAINER_FEMALE | 
#line 1726
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1727
        .doubleBattle = FALSE,
#line 1728
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1730
            .species = SPECIES_CHARCADET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1732
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1731
            .lvl = 18,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1733
            .species = SPECIES_SENTRET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1735
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1734
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1741
#line 1743
    [DIFFICULTY_EASY][TRAINER_GALECRESTGYM_LEADER] =
    {
#line 1742
        .trainerName = _("Kohla"),
#line 1744
        .trainerClass = TRAINER_CLASS_ACE_ROOKIE,
#line 1745
        .trainerPic = TRAINER_PIC_WALLY,
        .encounterMusic_gender =
#line 1747
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 1749
        .items = { ITEM_SUPER_POTION },
#line 1748
        .doubleBattle = FALSE,
#line 1750
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 1751
        .mugshotColor = MUGSHOT_COLOR_BLUE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 1753
            .species = SPECIES_YAMPER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1755
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 1754
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1757
            .species = SPECIES_KIRLIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1759
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 1758
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1761
            .species = SPECIES_DEWOTT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1763
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 1762
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1765
            .species = SPECIES_CERULEDGE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1765
            .heldItem = ITEM_ORAN_BERRY,
#line 1767
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 1766
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 1768
                MOVE_SHADOW_SNEAK,
                MOVE_WILL_O_WISP,
                MOVE_FLAME_CHARGE,
            },
            },
        },
    },
#line 1772
#line 1774
    [DIFFICULTY_NORMAL][TRAINER_GALECRESTGYM_LEADER] =
    {
#line 1773
        .trainerName = _("Kohla"),
#line 1775
        .trainerClass = TRAINER_CLASS_ACE_ROOKIE,
#line 1776
        .trainerPic = TRAINER_PIC_WALLY,
        .encounterMusic_gender =
#line 1778
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 1780
        .items = { ITEM_SUPER_POTION },
#line 1779
        .doubleBattle = FALSE,
#line 1781
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 1782
        .mugshotColor = MUGSHOT_COLOR_BLUE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 1784
            .species = SPECIES_YAMPER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1786
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1785
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1787
            .species = SPECIES_KIRLIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1787
            .heldItem = ITEM_ROCKY_HELMET,
#line 1789
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1788
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1790
            .species = SPECIES_DEWOTT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1792
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1791
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1793
            .species = SPECIES_CERULEDGE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1793
            .heldItem = ITEM_SITRUS_BERRY,
#line 1795
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 1794
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 1796
                MOVE_SHADOW_SNEAK,
                MOVE_SWORDS_DANCE,
                MOVE_WILL_O_WISP,
                MOVE_FLAME_CHARGE,
            },
            },
        },
    },
#line 1806
#line 1808
    [DIFFICULTY_EASY][TRAINER_VILETHORN_A] =
    {
#line 1807
        .trainerName = _("Yeni"),
#line 1809
        .trainerClass = TRAINER_CLASS_BATTLE_GIRL,
#line 1810
        .trainerPic = TRAINER_PIC_BATTLE_GIRL,
        .encounterMusic_gender =
#line 1811
F_TRAINER_FEMALE | 
#line 1812
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 1813
        .doubleBattle = FALSE,
#line 1814
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 1816
            .species = SPECIES_PASSIMIAN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1818
            .iv = TRAINER_PARTY_IVS(7, 7, 7, 7, 7, 7),
#line 1817
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1820
#line 1822
    [DIFFICULTY_NORMAL][TRAINER_VILETHORN_A] =
    {
#line 1821
        .trainerName = _("Yeni"),
#line 1823
        .trainerClass = TRAINER_CLASS_BATTLE_GIRL,
#line 1824
        .trainerPic = TRAINER_PIC_BATTLE_GIRL,
        .encounterMusic_gender =
#line 1825
F_TRAINER_FEMALE | 
#line 1826
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 1827
        .doubleBattle = FALSE,
#line 1828
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 1830
            .species = SPECIES_PASSIMIAN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1832
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1831
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1839
#line 1841
    [DIFFICULTY_EASY][TRAINER_VILETHORN_B] =
    {
#line 1840
        .trainerName = _("Dusty"),
#line 1842
        .trainerClass = TRAINER_CLASS_PSYCHIC,
#line 1843
        .trainerPic = TRAINER_PIC_PSYCHIC_M,
        .encounterMusic_gender =
#line 1845
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 1846
        .doubleBattle = FALSE,
#line 1847
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 1849
            .species = SPECIES_MORELULL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1851
            .iv = TRAINER_PARTY_IVS(7, 7, 7, 7, 7, 7),
#line 1850
            .lvl = 18,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1853
            .species = SPECIES_CHINGLING,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1855
            .iv = TRAINER_PARTY_IVS(7, 7, 7, 7, 7, 7),
#line 1854
            .lvl = 18,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1857
            .species = SPECIES_BRUXISH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1859
            .iv = TRAINER_PARTY_IVS(7, 7, 7, 7, 7, 7),
#line 1858
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1861
#line 1863
    [DIFFICULTY_NORMAL][TRAINER_VILETHORN_B] =
    {
#line 1862
        .trainerName = _("Dusty"),
#line 1864
        .trainerClass = TRAINER_CLASS_PSYCHIC,
#line 1865
        .trainerPic = TRAINER_PIC_PSYCHIC_M,
        .encounterMusic_gender =
#line 1867
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 1868
        .doubleBattle = FALSE,
#line 1869
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 1871
            .species = SPECIES_MORELULL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1873
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1872
            .lvl = 18,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1874
            .species = SPECIES_CHINGLING,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1876
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1875
            .lvl = 18,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1877
            .species = SPECIES_BRUXISH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1879
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1878
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1886
#line 1888
    [DIFFICULTY_EASY][TRAINER_VILETHORN_C] =
    {
#line 1887
        .trainerName = _("Patricia"),
#line 1889
        .trainerClass = TRAINER_CLASS_HEX_MANIAC,
#line 1890
        .trainerPic = TRAINER_PIC_HEX_MANIAC,
        .encounterMusic_gender =
#line 1891
F_TRAINER_FEMALE | 
#line 1892
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 1893
        .doubleBattle = FALSE,
#line 1894
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1896
            .species = SPECIES_POLTCHAGEIST,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1898
            .iv = TRAINER_PARTY_IVS(8, 8, 8, 8, 8, 8),
#line 1897
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1900
            .species = SPECIES_SHUPPET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1902
            .iv = TRAINER_PARTY_IVS(8, 8, 8, 8, 8, 8),
#line 1901
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1904
#line 1906
    [DIFFICULTY_NORMAL][TRAINER_VILETHORN_C] =
    {
#line 1905
        .trainerName = _("Patricia"),
#line 1907
        .trainerClass = TRAINER_CLASS_HEX_MANIAC,
#line 1908
        .trainerPic = TRAINER_PIC_HEX_MANIAC,
        .encounterMusic_gender =
#line 1909
F_TRAINER_FEMALE | 
#line 1910
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 1911
        .doubleBattle = FALSE,
#line 1912
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1914
            .species = SPECIES_POLTCHAGEIST,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1916
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1915
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1917
            .species = SPECIES_SHUPPET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1919
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1918
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1927
#line 1929
    [DIFFICULTY_EASY][TRAINER_VILETHORN_D] =
    {
#line 1928
        .trainerName = _("Isaac"),
#line 1930
        .trainerClass = TRAINER_CLASS_PKMN_BREEDER,
#line 1931
        .trainerPic = TRAINER_PIC_POKEMON_BREEDER_M,
        .encounterMusic_gender =
#line 1933
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 1934
        .doubleBattle = FALSE,
#line 1935
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1937
            .species = SPECIES_STANTLER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1939
            .iv = TRAINER_PARTY_IVS(9, 9, 9, 9, 9, 9),
#line 1938
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1941
            .species = SPECIES_PONYTA_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1943
            .iv = TRAINER_PARTY_IVS(9, 9, 9, 9, 9, 9),
#line 1942
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1945
#line 1947
    [DIFFICULTY_NORMAL][TRAINER_VILETHORN_D] =
    {
#line 1946
        .trainerName = _("Isaac"),
#line 1948
        .trainerClass = TRAINER_CLASS_PKMN_BREEDER,
#line 1949
        .trainerPic = TRAINER_PIC_POKEMON_BREEDER_M,
        .encounterMusic_gender =
#line 1951
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 1952
        .doubleBattle = FALSE,
#line 1953
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 1955
            .species = SPECIES_STANTLER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1957
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1956
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 1958
            .species = SPECIES_PONYTA_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1958
            .heldItem = ITEM_ORAN_BERRY,
#line 1960
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 1959
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1975
#line 1977
    [DIFFICULTY_EASY][TRAINER_VILETHORN_E] =
    {
#line 1976
        .trainerName = _("Melissa"),
#line 1978
        .trainerClass = TRAINER_CLASS_BEAUTY,
#line 1979
        .trainerPic = TRAINER_PIC_BEAUTY,
        .encounterMusic_gender =
#line 1980
F_TRAINER_FEMALE | 
#line 1981
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1982
        .doubleBattle = FALSE,
#line 1983
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 1985
            .species = SPECIES_ROSELIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 1987
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 1986
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 1989
#line 1991
    [DIFFICULTY_NORMAL][TRAINER_VILETHORN_E] =
    {
#line 1990
        .trainerName = _("Melissa"),
#line 1992
        .trainerClass = TRAINER_CLASS_BEAUTY,
#line 1993
        .trainerPic = TRAINER_PIC_BEAUTY,
        .encounterMusic_gender =
#line 1994
F_TRAINER_FEMALE | 
#line 1995
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 1996
        .doubleBattle = FALSE,
#line 1997
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 1999
            .species = SPECIES_ROSELIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2001
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2000
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2015
#line 2017
    [DIFFICULTY_EASY][TRAINER_VILETHORN_F] =
    {
#line 2016
        .trainerName = _("Gabby & Ty"),
#line 2018
        .trainerClass = TRAINER_CLASS_INTERVIEWER,
#line 2019
        .trainerPic = TRAINER_PIC_INTERVIEWER,
        .encounterMusic_gender =
#line 2021
            TRAINER_ENCOUNTER_MUSIC_INTERVIEWER,
#line 2022
        .doubleBattle = TRUE,
#line 2023
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2025
            .species = SPECIES_MAGNEMITE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2027
            .iv = TRAINER_PARTY_IVS(6, 6, 6, 6, 6, 6),
#line 2026
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2029
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2031
            .iv = TRAINER_PARTY_IVS(6, 6, 6, 6, 6, 6),
#line 2030
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2033
#line 2035
    [DIFFICULTY_NORMAL][TRAINER_VILETHORN_F] =
    {
#line 2034
        .trainerName = _("Gabby & Ty"),
#line 2036
        .trainerClass = TRAINER_CLASS_INTERVIEWER,
#line 2037
        .trainerPic = TRAINER_PIC_INTERVIEWER,
        .encounterMusic_gender =
#line 2039
            TRAINER_ENCOUNTER_MUSIC_INTERVIEWER,
#line 2040
        .doubleBattle = TRUE,
#line 2041
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2043
            .species = SPECIES_MAGNEMITE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2045
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2044
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2046
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2048
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2047
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2055
#line 2057
    [DIFFICULTY_EASY][TRAINER_VILETHORN_G] =
    {
#line 2056
        .trainerName = _("Stanja"),
#line 2058
        .trainerClass = TRAINER_CLASS_BUG_MANIAC,
#line 2059
        .trainerPic = TRAINER_PIC_BUG_MANIAC,
        .encounterMusic_gender =
#line 2061
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 2062
        .doubleBattle = FALSE,
#line 2063
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 2064
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 2066
            .species = SPECIES_DOTTLER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2068
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2067
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2070
            .species = SPECIES_DEWPIDER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2072
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2071
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2074
            .species = SPECIES_LOKIX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2076
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2075
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2078
            .species = SPECIES_PINSIR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2080
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2079
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2082
#line 2084
    [DIFFICULTY_NORMAL][TRAINER_VILETHORN_G] =
    {
#line 2083
        .trainerName = _("Stanja"),
#line 2085
        .trainerClass = TRAINER_CLASS_BUG_MANIAC,
#line 2086
        .trainerPic = TRAINER_PIC_BUG_MANIAC,
        .encounterMusic_gender =
#line 2088
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 2090
        .items = { ITEM_SUPER_POTION },
#line 2089
        .doubleBattle = FALSE,
#line 2091
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON | AI_FLAG_PREDICTION,
#line 2092
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 2094
            .species = SPECIES_DOTTLER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2094
            .heldItem = ITEM_ORAN_BERRY,
#line 2096
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2095
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2097
            .species = SPECIES_DEWPIDER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2099
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2098
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2100
            .species = SPECIES_LOKIX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2100
            .heldItem = ITEM_BUG_GEM,
#line 2102
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2101
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2103
            .species = SPECIES_PINSIR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2103
            .heldItem = ITEM_LEFTOVERS,
#line 2105
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2104
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2112
#line 2114
    [DIFFICULTY_EASY][TRAINER_VILETHORN_H] =
    {
#line 2113
        .trainerName = _("Ty"),
#line 2115
        .trainerClass = TRAINER_CLASS_BURGLAR,
#line 2116
        .trainerPic = TRAINER_PIC_BURGLAR,
        .encounterMusic_gender =
#line 2118
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 2119
        .doubleBattle = FALSE,
#line 2120
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2122
            .species = SPECIES_NICKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2124
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2123
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2126
            .species = SPECIES_RATTATA_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2128
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2127
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2130
#line 2132
    [DIFFICULTY_NORMAL][TRAINER_VILETHORN_H] =
    {
#line 2131
        .trainerName = _("Ty"),
#line 2133
        .trainerClass = TRAINER_CLASS_BURGLAR,
#line 2134
        .trainerPic = TRAINER_PIC_BURGLAR,
        .encounterMusic_gender =
#line 2136
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 2137
        .doubleBattle = FALSE,
#line 2138
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2140
            .species = SPECIES_NICKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2142
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2141
            .lvl = 19,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2143
            .species = SPECIES_RATTATA_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2145
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2144
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2158
#line 2160
    [DIFFICULTY_EASY][TRAINER_VILETHORN_I] =
    {
#line 2159
        .trainerName = _("Shoe"),
#line 2161
        .trainerClass = TRAINER_CLASS_GENTLEMAN,
#line 2162
        .trainerPic = TRAINER_PIC_GENTLEMAN,
        .encounterMusic_gender =
#line 2164
            TRAINER_ENCOUNTER_MUSIC_INTERVIEWER,
#line 2165
        .doubleBattle = TRUE,
#line 2166
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2168
            .species = SPECIES_GROWLITHE_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2170
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2169
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2172
            .species = SPECIES_HERDIER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2174
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2173
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2176
#line 2178
    [DIFFICULTY_NORMAL][TRAINER_VILETHORN_I] =
    {
#line 2177
        .trainerName = _("Shoe"),
#line 2179
        .trainerClass = TRAINER_CLASS_GENTLEMAN,
#line 2180
        .trainerPic = TRAINER_PIC_GENTLEMAN,
        .encounterMusic_gender =
#line 2182
            TRAINER_ENCOUNTER_MUSIC_INTERVIEWER,
#line 2183
        .doubleBattle = TRUE,
#line 2184
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2186
            .species = SPECIES_GROWLITHE_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2186
            .heldItem = ITEM_LIECHI_BERRY,
#line 2189
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2187
            .ability = ABILITY_INTIMIDATE,
#line 2188
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 2189
                MOVE_FLAME_CHARGE,
            },
            },
            {
#line 2191
            .species = SPECIES_HERDIER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2193
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2192
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2210
#line 2212
    [DIFFICULTY_EASY][TRAINER_ROUTE5_A] =
    {
#line 2211
        .trainerName = _("Lola"),
#line 2213
        .trainerClass = TRAINER_CLASS_TUBER_F,
#line 2214
        .trainerPic = TRAINER_PIC_TUBER_F,
        .encounterMusic_gender =
#line 2215
F_TRAINER_FEMALE | 
#line 2216
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 2217
        .doubleBattle = FALSE,
#line 2218
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2220
            .species = SPECIES_AZURILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2222
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 2221
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2224
            .species = SPECIES_AZURILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2226
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 2225
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2228
#line 2230
    [DIFFICULTY_EASY][TRAINER_ROUTE5_B] =
    {
#line 2229
        .trainerName = _("AUSTINA"),
#line 2231
        .trainerClass = TRAINER_CLASS_TUBER_F,
#line 2232
        .trainerPic = TRAINER_PIC_TUBER_F,
        .encounterMusic_gender =
#line 2233
F_TRAINER_FEMALE | 
#line 2234
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 2235
        .doubleBattle = FALSE,
#line 2236
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2238
            .species = SPECIES_MARILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2240
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 2239
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2242
#line 2244
    [DIFFICULTY_EASY][TRAINER_ROUTE5_C] =
    {
#line 2243
        .trainerName = _("GWEN"),
#line 2245
        .trainerClass = TRAINER_CLASS_TUBER_F,
#line 2246
        .trainerPic = TRAINER_PIC_TUBER_F,
        .encounterMusic_gender =
#line 2247
F_TRAINER_FEMALE | 
#line 2248
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 2249
        .doubleBattle = FALSE,
#line 2250
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2252
            .species = SPECIES_MARILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2254
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 2253
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2256
#line 2258
    [DIFFICULTY_EASY][TRAINER_ROUTE5_D] =
    {
#line 2257
        .trainerName = _("LOLA"),
#line 2259
        .trainerClass = TRAINER_CLASS_TUBER_F,
#line 2260
        .trainerPic = TRAINER_PIC_TUBER_F,
        .encounterMusic_gender =
#line 2261
F_TRAINER_FEMALE | 
#line 2262
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 2263
        .doubleBattle = FALSE,
#line 2264
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2266
            .species = SPECIES_MARILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2268
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 2267
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2270
            .species = SPECIES_MARILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2272
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 2271
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2289
#line 2291
    [DIFFICULTY_EASY][TRAINER_SEWERS_A] =
    {
#line 2290
        .trainerName = _("Gondor"),
#line 2292
        .trainerClass = TRAINER_CLASS_RICH_BOY,
#line 2293
        .trainerPic = TRAINER_PIC_RICH_BOY,
        .encounterMusic_gender =
#line 2295
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 2296
        .doubleBattle = FALSE,
#line 2297
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2299
            .species = SPECIES_GRIMER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2302
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 2300
            .lvl = 23,
            .nature = NATURE_HARDY,
#line 2301
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2304
            .species = SPECIES_GURDURR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2307
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 2305
            .lvl = 24,
            .nature = NATURE_HARDY,
#line 2306
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2309
#line 2311
    [DIFFICULTY_NORMAL][TRAINER_SEWERS_A] =
    {
#line 2310
        .trainerName = _("Gondor"),
#line 2312
        .trainerClass = TRAINER_CLASS_RICH_BOY,
#line 2313
        .trainerPic = TRAINER_PIC_RICH_BOY,
        .encounterMusic_gender =
#line 2315
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 2316
        .doubleBattle = FALSE,
#line 2317
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2319
            .species = SPECIES_GRIMER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2322
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2320
            .lvl = 23,
            .nature = NATURE_HARDY,
#line 2321
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2323
            .species = SPECIES_GURDURR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2326
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2324
            .lvl = 24,
            .nature = NATURE_HARDY,
#line 2325
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2338
#line 2340
    [DIFFICULTY_EASY][TRAINER_SEWERS_B] =
    {
#line 2339
        .trainerName = _("Tinglia"),
#line 2341
        .trainerClass = TRAINER_CLASS_HEX_MANIAC,
#line 2342
        .trainerPic = TRAINER_PIC_HEX_MANIAC,
        .encounterMusic_gender =
#line 2343
F_TRAINER_FEMALE | 
#line 2344
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 2345
        .doubleBattle = FALSE,
#line 2346
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2348
            .species = SPECIES_LITWICK,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2350
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 2349
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2352
#line 2354
    [DIFFICULTY_NORMAL][TRAINER_SEWERS_B] =
    {
#line 2353
        .trainerName = _("Tinglia"),
#line 2355
        .trainerClass = TRAINER_CLASS_HEX_MANIAC,
#line 2356
        .trainerPic = TRAINER_PIC_HEX_MANIAC,
        .encounterMusic_gender =
#line 2357
F_TRAINER_FEMALE | 
#line 2358
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 2359
        .doubleBattle = FALSE,
#line 2360
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2362
            .species = SPECIES_LITWICK,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2364
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2363
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2375
#line 2377
    [DIFFICULTY_EASY][TRAINER_SEWERS_C] =
    {
#line 2376
        .trainerName = _("Kirk"),
#line 2378
        .trainerClass = TRAINER_CLASS_GUITARIST,
#line 2379
        .trainerPic = TRAINER_PIC_GUITARIST,
        .encounterMusic_gender =
#line 2381
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 2382
        .doubleBattle = FALSE,
#line 2383
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2385
            .species = SPECIES_VOLTORB_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2387
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2386
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2389
            .species = SPECIES_TOXEL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2391
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2390
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2393
#line 2395
    [DIFFICULTY_NORMAL][TRAINER_SEWERS_C] =
    {
#line 2394
        .trainerName = _("Kirk"),
#line 2396
        .trainerClass = TRAINER_CLASS_GUITARIST,
#line 2397
        .trainerPic = TRAINER_PIC_GUITARIST,
        .encounterMusic_gender =
#line 2399
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 2400
        .doubleBattle = FALSE,
#line 2401
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2403
            .species = SPECIES_VOLTORB_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2405
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2404
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2406
            .species = SPECIES_TOXEL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2406
            .heldItem = ITEM_BLACK_SLUDGE,
#line 2408
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2407
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2423
#line 2425
    [DIFFICULTY_EASY][TRAINER_SEWERS_D] =
    {
#line 2424
        .trainerName = _("RICKY"),
#line 2426
        .trainerClass = TRAINER_CLASS_TUBER_M,
#line 2427
        .trainerPic = TRAINER_PIC_TUBER_M,
        .encounterMusic_gender =
#line 2429
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 2430
        .doubleBattle = FALSE,
#line 2431
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2433
            .species = SPECIES_ZIGZAGOON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2435
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 2434
            .lvl = 13,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 2436
                MOVE_SAND_ATTACK,
                MOVE_HEADBUTT,
                MOVE_TAIL_WHIP,
                MOVE_SURF,
            },
            },
        },
    },
#line 2441
#line 2443
    [DIFFICULTY_EASY][TRAINER_SEWERS_E] =
    {
#line 2442
        .trainerName = _("SIMON"),
#line 2444
        .trainerClass = TRAINER_CLASS_TUBER_M,
#line 2445
        .trainerPic = TRAINER_PIC_TUBER_M,
        .encounterMusic_gender =
#line 2447
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 2448
        .doubleBattle = FALSE,
#line 2449
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2451
            .species = SPECIES_AZURILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2453
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 2452
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2455
            .species = SPECIES_MARILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2457
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 2456
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2469
#line 2471
    [DIFFICULTY_EASY][TRAINER_SILVERSUNGYM_A] =
    {
#line 2470
        .trainerName = _("Rosanna"),
#line 2472
        .trainerClass = TRAINER_CLASS_BEAUTY,
#line 2473
        .trainerPic = TRAINER_PIC_BEAUTY,
        .encounterMusic_gender =
#line 2474
F_TRAINER_FEMALE | 
#line 2475
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 2476
        .doubleBattle = FALSE,
#line 2477
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2479
            .species = SPECIES_ROSELIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2481
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 2480
            .lvl = 24,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2483
#line 2485
    [DIFFICULTY_NORMAL][TRAINER_SILVERSUNGYM_A] =
    {
#line 2484
        .trainerName = _("Rosanna"),
#line 2486
        .trainerClass = TRAINER_CLASS_BEAUTY,
#line 2487
        .trainerPic = TRAINER_PIC_BEAUTY,
        .encounterMusic_gender =
#line 2488
F_TRAINER_FEMALE | 
#line 2489
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 2490
        .doubleBattle = FALSE,
#line 2491
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2493
            .species = SPECIES_ROSELIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2495
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2494
            .lvl = 24,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2506
#line 2508
    [DIFFICULTY_EASY][TRAINER_SILVERSUNGYM_B] =
    {
#line 2507
        .trainerName = _("Johnston"),
#line 2509
        .trainerClass = TRAINER_CLASS_MODEL,
#line 2510
        .trainerPic = TRAINER_PIC_MODEL,
        .encounterMusic_gender =
#line 2512
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 2513
        .doubleBattle = FALSE,
#line 2514
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2516
            .species = SPECIES_ZIGZAGOON_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2518
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 2517
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2520
            .species = SPECIES_BAYLEEF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2522
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 2521
            .lvl = 24,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2524
#line 2526
    [DIFFICULTY_NORMAL][TRAINER_SILVERSUNGYM_B] =
    {
#line 2525
        .trainerName = _("Johnston"),
#line 2527
        .trainerClass = TRAINER_CLASS_MODEL,
#line 2528
        .trainerPic = TRAINER_PIC_MODEL,
        .encounterMusic_gender =
#line 2530
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 2531
        .doubleBattle = FALSE,
#line 2532
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2534
            .species = SPECIES_ZIGZAGOON_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2536
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2535
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2537
            .species = SPECIES_BAYLEEF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2539
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2538
            .lvl = 24,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2547
#line 2549
    [DIFFICULTY_EASY][TRAINER_SILVERSUNGYM_C] =
    {
#line 2548
        .trainerName = _("Astra"),
#line 2550
        .trainerClass = TRAINER_CLASS_BEAUTY,
#line 2551
        .trainerPic = TRAINER_PIC_BEAUTY,
        .encounterMusic_gender =
#line 2552
F_TRAINER_FEMALE | 
#line 2553
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 2554
        .doubleBattle = FALSE,
#line 2555
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 2557
            .species = SPECIES_PETILIL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2559
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 2558
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2561
            .species = SPECIES_BUDEW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2563
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 2562
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2565
            .species = SPECIES_ZIGZAGOON_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2567
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 2566
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2569
#line 2571
    [DIFFICULTY_NORMAL][TRAINER_SILVERSUNGYM_C] =
    {
#line 2570
        .trainerName = _("Astra"),
#line 2572
        .trainerClass = TRAINER_CLASS_BEAUTY,
#line 2573
        .trainerPic = TRAINER_PIC_BEAUTY,
        .encounterMusic_gender =
#line 2574
F_TRAINER_FEMALE | 
#line 2575
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 2576
        .doubleBattle = FALSE,
#line 2577
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 2579
            .species = SPECIES_PETILIL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2581
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2580
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2582
            .species = SPECIES_BUDEW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2584
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2583
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2585
            .species = SPECIES_ZIGZAGOON_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2587
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2586
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2601
#line 2603
    [DIFFICULTY_EASY][TRAINER_SILVERSUNGYM_D] =
    {
#line 2602
        .trainerName = _("Caster"),
#line 2604
        .trainerClass = TRAINER_CLASS_MODEL,
#line 2605
        .trainerPic = TRAINER_PIC_MODEL,
        .encounterMusic_gender =
#line 2607
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 2608
        .doubleBattle = FALSE,
#line 2609
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2611
            .species = SPECIES_LINOONE_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2613
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 2612
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2615
#line 2617
    [DIFFICULTY_NORMAL][TRAINER_SILVERSUNGYM_D] =
    {
#line 2616
        .trainerName = _("Caster"),
#line 2618
        .trainerClass = TRAINER_CLASS_MODEL,
#line 2619
        .trainerPic = TRAINER_PIC_MODEL,
        .encounterMusic_gender =
#line 2621
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 2622
        .doubleBattle = FALSE,
#line 2623
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2625
            .species = SPECIES_LINOONE_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2625
            .heldItem = ITEM_SITRUS_BERRY,
#line 2627
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2626
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2639
#line 2641
    [DIFFICULTY_EASY][TRAINER_SILVERSUNGYM_LEADER] =
    {
#line 2640
        .trainerName = _("Gloria"),
#line 2642
        .trainerClass = TRAINER_CLASS_LEADER,
#line 2643
        .trainerPic = TRAINER_PIC_LEADER_GLORIA,
        .encounterMusic_gender =
#line 2644
F_TRAINER_FEMALE | 
#line 2645
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 2646
        .items = { ITEM_SUPER_POTION, ITEM_SUPER_POTION },
#line 2647
        .doubleBattle = FALSE,
#line 2648
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 2649
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 2651
            .species = SPECIES_BAYLEEF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2653
            .iv = TRAINER_PARTY_IVS(16, 16, 16, 16, 16, 16),
#line 2652
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2655
            .species = SPECIES_LILLIGANT_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2657
            .iv = TRAINER_PARTY_IVS(16, 16, 16, 16, 16, 16),
#line 2656
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2659
            .species = SPECIES_LINOONE_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2659
            .heldItem = ITEM_SITRUS_BERRY,
#line 2661
            .iv = TRAINER_PARTY_IVS(16, 16, 16, 16, 16, 16),
#line 2660
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2663
            .species = SPECIES_BOMBIRDIER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2663
            .heldItem = ITEM_FLYING_GEM,
#line 2665
            .iv = TRAINER_PARTY_IVS(16, 16, 16, 16, 16, 16),
#line 2664
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2667
#line 2669
    [DIFFICULTY_NORMAL][TRAINER_SILVERSUNGYM_LEADER] =
    {
#line 2668
        .trainerName = _("Gloria"),
#line 2670
        .trainerClass = TRAINER_CLASS_LEADER,
#line 2671
        .trainerPic = TRAINER_PIC_LEADER_GLORIA,
        .encounterMusic_gender =
#line 2672
F_TRAINER_FEMALE | 
#line 2673
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 2674
        .items = { ITEM_SUPER_POTION, ITEM_SUPER_POTION },
#line 2675
        .doubleBattle = FALSE,
#line 2676
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_FORCE_SETUP_FIRST_TURN | AI_FLAG_ACE_POKEMON,
#line 2677
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 2679
            .species = SPECIES_BAYLEEF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2679
            .heldItem = ITEM_LIGHT_CLAY,
#line 2681
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2680
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 2681
                MOVE_SUNNY_DAY,
                MOVE_MAGICAL_LEAF,
                MOVE_SYNTHESIS,
                MOVE_STOMPING_TANTRUM,
            },
            },
            {
#line 2686
            .species = SPECIES_ROSERADE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2686
            .heldItem = ITEM_BIG_ROOT,
#line 2688
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2687
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 2688
                MOVE_GROWTH,
                MOVE_GIGA_DRAIN,
                MOVE_INGRAIN,
                MOVE_SLUDGE_BOMB,
            },
            },
            {
#line 2693
            .species = SPECIES_LINOONE_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2693
            .heldItem = ITEM_SITRUS_BERRY,
#line 2695
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2694
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 2695
                MOVE_BELLY_DRUM,
                MOVE_EXTREMESPEED,
                MOVE_NIGHT_SLASH,
            },
            },
            {
#line 2700
            .species = SPECIES_BOMBIRDIER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2700
            .heldItem = ITEM_ROCK_GEM,
#line 2703
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2701
            .ability = ABILITY_ROCKY_PAYLOAD,
#line 2702
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 2703
                MOVE_ROCK_SLIDE,
                MOVE_ACROBATICS,
                MOVE_KNOCK_OFF,
            },
            },
        },
    },
#line 2718
#line 2720
    [DIFFICULTY_EASY][TRAINER_THEATER_A] =
    {
#line 2719
        .trainerName = _("Randel"),
#line 2721
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 2722
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 2724
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 2725
        .items = { ITEM_HYPER_POTION },
#line 2726
        .doubleBattle = FALSE,
#line 2727
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2729
            .species = SPECIES_SWELLOW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2731
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2730
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 2732
                MOVE_QUICK_ATTACK,
                MOVE_AGILITY,
                MOVE_WING_ATTACK,
            },
            },
        },
    },
#line 2744
#line 2746
    [DIFFICULTY_EASY][TRAINER_THEATER_B] =
    {
#line 2745
        .trainerName = _("Pillin"),
#line 2747
        .trainerClass = TRAINER_CLASS_DRAGON_TAMER,
#line 2748
        .trainerPic = TRAINER_PIC_DRAGON_TAMER,
        .encounterMusic_gender =
#line 2750
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 2751
        .doubleBattle = FALSE,
#line 2752
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2754
            .species = SPECIES_APPLIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2756
            .iv = TRAINER_PARTY_IVS(8, 8, 8, 8, 8, 8),
#line 2755
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2758
#line 2760
    [DIFFICULTY_NORMAL][TRAINER_THEATER_B] =
    {
#line 2759
        .trainerName = _("Pillin"),
#line 2761
        .trainerClass = TRAINER_CLASS_DRAGON_TAMER,
#line 2762
        .trainerPic = TRAINER_PIC_DRAGON_TAMER,
        .encounterMusic_gender =
#line 2764
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 2765
        .items = { ITEM_HYPER_POTION },
#line 2766
        .doubleBattle = FALSE,
#line 2767
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2769
            .species = SPECIES_APPLIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2769
            .heldItem = ITEM_SITRUS_BERRY,
#line 2771
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2770
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2783
#line 2785
    [DIFFICULTY_EASY][TRAINER_SOMBERHQ_A] =
    {
#line 2784
        .trainerName = _("Grunt"),
#line 2786
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 2787
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 2789
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 2790
        .doubleBattle = FALSE,
#line 2791
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2793
            .species = SPECIES_LOKIX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2795
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2794
            .lvl = 24,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2797
#line 2799
    [DIFFICULTY_NORMAL][TRAINER_SOMBERHQ_A] =
    {
#line 2798
        .trainerName = _("Grunt"),
#line 2800
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 2801
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 2803
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 2804
        .doubleBattle = FALSE,
#line 2805
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2807
            .species = SPECIES_LOKIX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2807
            .heldItem = ITEM_BUG_GEM,
#line 2810
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2808
            .ability = ABILITY_TINTED_LENS,
#line 2809
            .lvl = 24,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 2810
                MOVE_LEECH_LIFE,
                MOVE_ASSURANCE,
            },
            },
        },
    },
#line 2821
#line 2823
    [DIFFICULTY_EASY][TRAINER_SOMBERHQ_B] =
    {
#line 2822
        .trainerName = _("Grunt"),
#line 2824
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 2825
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 2827
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 2828
        .doubleBattle = FALSE,
#line 2829
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2831
            .species = SPECIES_BRONZOR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2833
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2832
            .lvl = 24,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2835
            .species = SPECIES_GRIMER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2837
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2836
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2839
#line 2841
    [DIFFICULTY_NORMAL][TRAINER_SOMBERHQ_B] =
    {
#line 2840
        .trainerName = _("Grunt"),
#line 2842
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 2843
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 2845
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 2846
        .doubleBattle = FALSE,
#line 2847
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2849
            .species = SPECIES_BRONZOR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2849
            .heldItem = ITEM_COLBUR_BERRY,
#line 2851
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2850
            .lvl = 24,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2852
            .species = SPECIES_GRIMER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2852
            .heldItem = ITEM_BLACK_SLUDGE,
#line 2854
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2853
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2869
#line 2871
    [DIFFICULTY_EASY][TRAINER_SOMBERHQ_C] =
    {
#line 2870
        .trainerName = _("Grunt"),
#line 2872
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 2873
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 2875
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 2876
        .doubleBattle = FALSE,
#line 2877
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2879
            .species = SPECIES_YANMA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2881
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2880
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2883
#line 2885
    [DIFFICULTY_NORMAL][TRAINER_SOMBERHQ_C] =
    {
#line 2884
        .trainerName = _("Grunt"),
#line 2886
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 2887
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 2889
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 2891
        .items = { ITEM_SUPER_POTION },
#line 2890
        .doubleBattle = FALSE,
#line 2892
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 2894
            .species = SPECIES_YANMA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2894
            .heldItem = ITEM_PETAYA_BERRY,
#line 2897
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2895
            .ability = ABILITY_SPEED_BOOST,
#line 2896
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2905
#line 2907
    [DIFFICULTY_EASY][TRAINER_SOMBERHQ_D] =
    {
#line 2906
        .trainerName = _("Grunt"),
#line 2908
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 2909
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 2911
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 2912
        .doubleBattle = FALSE,
#line 2913
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2915
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2917
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2916
            .lvl = 24,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2919
            .species = SPECIES_LOKIX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2921
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2920
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2923
#line 2925
    [DIFFICULTY_NORMAL][TRAINER_SOMBERHQ_D] =
    {
#line 2924
        .trainerName = _("Grunt"),
#line 2926
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 2927
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 2929
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 2930
        .doubleBattle = FALSE,
#line 2931
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2933
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2935
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2934
            .lvl = 24,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2936
            .species = SPECIES_LOKIX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2938
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2937
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2950
#line 2952
    [DIFFICULTY_EASY][TRAINER_SOMBERHQ_E] =
    {
#line 2951
        .trainerName = _("Grunt"),
#line 2953
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 2954
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 2956
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 2957
        .doubleBattle = FALSE,
#line 2958
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2960
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2962
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2961
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2964
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2966
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 2965
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2968
#line 2970
    [DIFFICULTY_NORMAL][TRAINER_SOMBERHQ_E] =
    {
#line 2969
        .trainerName = _("Grunt"),
#line 2971
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 2972
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 2974
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 2975
        .doubleBattle = FALSE,
#line 2976
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 2978
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2980
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2979
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 2981
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 2983
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 2982
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 2996
#line 2998
    [DIFFICULTY_EASY][TRAINER_SOMBERHQ_F] =
    {
#line 2997
        .trainerName = _("Grunt"),
#line 2999
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 3000
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 3002
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 3003
        .doubleBattle = FALSE,
#line 3004
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3006
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3008
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3007
            .lvl = 24,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3010
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3012
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3011
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3014
#line 3016
    [DIFFICULTY_NORMAL][TRAINER_SOMBERHQ_F] =
    {
#line 3015
        .trainerName = _("Grunt"),
#line 3017
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 3018
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 3020
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 3021
        .doubleBattle = FALSE,
#line 3022
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3024
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3026
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3025
            .lvl = 24,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3027
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3027
            .heldItem = ITEM_ORAN_BERRY,
#line 3029
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3028
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3043
#line 3045
    [DIFFICULTY_EASY][TRAINER_SOMBERHQ_G] =
    {
#line 3044
        .trainerName = _("Grunt"),
#line 3046
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 3047
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 3049
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 3050
        .doubleBattle = FALSE,
#line 3051
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3053
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3055
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3054
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3057
            .species = SPECIES_GRIMER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3059
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3058
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3061
#line 3063
    [DIFFICULTY_NORMAL][TRAINER_SOMBERHQ_G] =
    {
#line 3062
        .trainerName = _("Grunt"),
#line 3064
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 3065
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 3067
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 3068
        .doubleBattle = FALSE,
#line 3069
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3071
            .species = SPECIES_IMPIDIMP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3073
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3072
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3074
            .species = SPECIES_GRIMER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3074
            .heldItem = ITEM_BLACK_SLUDGE,
#line 3076
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3075
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3087
#line 3089
    [DIFFICULTY_EASY][TRAINER_SOMBERHQ_H] =
    {
#line 3088
        .trainerName = _("Grunt"),
#line 3090
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 3091
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 3093
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 3094
        .doubleBattle = FALSE,
#line 3095
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3097
            .species = SPECIES_LOKIX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3099
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3098
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3101
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3103
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3102
            .lvl = 27,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3105
#line 3107
    [DIFFICULTY_NORMAL][TRAINER_SOMBERHQ_H] =
    {
#line 3106
        .trainerName = _("Grunt"),
#line 3108
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 3109
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 3111
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 3112
        .doubleBattle = FALSE,
#line 3113
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3115
            .species = SPECIES_LOKIX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3117
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3116
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3118
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3120
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3119
            .lvl = 27,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3132
#line 3134
    [DIFFICULTY_EASY][TRAINER_SOMBERHQ_MELEA] =
    {
#line 3133
        .trainerName = _("Melea"),
#line 3135
        .trainerClass = TRAINER_CLASS_SOMBER_ADMIN,
#line 3136
        .trainerPic = TRAINER_PIC_SOMBER_ADMIN_MELEA,
        .encounterMusic_gender =
#line 3137
F_TRAINER_FEMALE | 
#line 3138
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 3139
        .doubleBattle = FALSE,
#line 3140
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 3141
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 3143
            .species = SPECIES_SLOWPOKE_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3145
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3144
            .lvl = 27,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3147
            .species = SPECIES_GRIMER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3147
            .heldItem = ITEM_BLACK_SLUDGE,
#line 3149
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3148
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3150
                MOVE_TOXIC,
                MOVE_POISON_FANG,
                MOVE_ROCK_SLIDE,
            },
            },
            {
#line 3154
            .species = SPECIES_YANMEGA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3157
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3155
            .ability = ABILITY_SPEED_BOOST,
#line 3156
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3158
                MOVE_AIR_SLASH,
                MOVE_BUG_BUZZ,
                MOVE_ANCIENT_POWER,
                MOVE_HYPNOSIS,
            },
            },
            {
#line 3163
            .species = SPECIES_ABSOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3165
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3164
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3167
#line 3169
    [DIFFICULTY_NORMAL][TRAINER_SOMBERHQ_MELEA] =
    {
#line 3168
        .trainerName = _("Melea"),
#line 3170
        .trainerClass = TRAINER_CLASS_SOMBER_ADMIN,
#line 3171
        .trainerPic = TRAINER_PIC_SOMBER_ADMIN_MELEA,
        .encounterMusic_gender =
#line 3172
F_TRAINER_FEMALE | 
#line 3173
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 3175
        .items = { ITEM_FULL_RESTORE },
#line 3174
        .doubleBattle = FALSE,
#line 3176
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_FORCE_SETUP_FIRST_TURN | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 3177
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 3179
            .species = SPECIES_YANMEGA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3179
            .heldItem = ITEM_PETAYA_BERRY,
#line 3183
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3181
            .ability = ABILITY_SPEED_BOOST,
#line 3182
            .lvl = 28,
#line 3180
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3183
                MOVE_AIR_SLASH,
                MOVE_BUG_BUZZ,
                MOVE_ANCIENT_POWER,
            },
            },
            {
#line 3187
            .species = SPECIES_SLOWPOKE_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3187
            .heldItem = ITEM_LIGHT_CLAY,
#line 3189
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3188
            .lvl = 27,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3189
                MOVE_LIGHT_SCREEN,
                MOVE_ZEN_HEADBUTT,
                MOVE_LIQUIDATION,
                MOVE_YAWN,
            },
            },
            {
#line 3194
            .species = SPECIES_GRIMER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3194
            .heldItem = ITEM_POISON_BARB,
#line 3196
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3195
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3196
                MOVE_TOXIC,
                MOVE_FLING,
                MOVE_VENOSHOCK,
                MOVE_ROCK_SLIDE,
            },
            },
            {
#line 3201
            .species = SPECIES_ABSOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3201
            .heldItem = ITEM_LIFE_ORB,
#line 3204
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3203
            .lvl = 29,
#line 3202
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3204
                MOVE_KNOCK_OFF,
                MOVE_SUCKER_PUNCH,
                MOVE_SWORDS_DANCE,
                MOVE_PLAY_ROUGH,
            },
            },
        },
    },
#line 3222
#line 3224
    [DIFFICULTY_EASY][TRAINER_ROUTE6_KOHLA] =
    {
#line 3223
        .trainerName = _("Kohla"),
#line 3225
        .trainerClass = TRAINER_CLASS_ACE_ROOKIE,
#line 3226
        .trainerPic = TRAINER_PIC_WALLY,
        .encounterMusic_gender =
#line 3228
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 3229
        .items = { ITEM_SUPER_POTION },
#line 3230
        .doubleBattle = FALSE,
#line 3231
        .aiFlags = AI_FLAG_BASIC_TRAINER | AI_FLAG_ACE_POKEMON,
#line 3232
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 3234
            .species = SPECIES_BOLTUND,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3236
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 3235
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3238
            .species = SPECIES_KIRLIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3240
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 3239
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3242
            .species = SPECIES_SCYTHER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3244
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 3243
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3246
            .species = SPECIES_DEWOTT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3248
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 3247
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3250
            .species = SPECIES_CERULEDGE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3250
            .heldItem = ITEM_SITRUS_BERRY,
#line 3252
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 3251
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3253
                MOVE_SWORDS_DANCE,
                MOVE_SHADOW_SNEAK,
                MOVE_WILL_O_WISP,
                MOVE_FLAME_CHARGE,
            },
            },
        },
    },
#line 3258
#line 3260
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_KOHLA] =
    {
#line 3259
        .trainerName = _("Kohla"),
#line 3261
        .trainerClass = TRAINER_CLASS_ACE_ROOKIE,
#line 3262
        .trainerPic = TRAINER_PIC_WALLY,
        .encounterMusic_gender =
#line 3264
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 3265
        .items = { ITEM_SUPER_POTION },
#line 3266
        .doubleBattle = FALSE,
#line 3267
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 3268
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 3270
            .species = SPECIES_BOLTUND,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3270
            .heldItem = ITEM_LEFTOVERS,
#line 3272
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3271
            .lvl = 25,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3273
            .species = SPECIES_KIRLIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3273
            .heldItem = ITEM_ROCKY_HELMET,
#line 3275
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3274
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3275
                MOVE_CALM_MIND,
                MOVE_THUNDER_WAVE,
                MOVE_STORED_POWER,
            },
            },
            {
#line 3279
            .species = SPECIES_SCYTHER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3279
            .heldItem = ITEM_FLYING_GEM,
#line 3283
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3281
            .ability = ABILITY_TECHNICIAN,
#line 3282
            .lvl = 28,
#line 3280
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3283
                MOVE_DUAL_WINGBEAT,
                MOVE_THIEF,
                MOVE_BUG_BITE,
            },
            },
            {
#line 3287
            .species = SPECIES_DEWOTT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3287
            .heldItem = ITEM_KINGS_ROCK,
#line 3289
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3288
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3290
            .species = SPECIES_CERULEDGE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3290
            .heldItem = ITEM_SITRUS_BERRY,
#line 3293
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3292
            .lvl = 31,
#line 3291
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3293
                MOVE_SWORDS_DANCE,
                MOVE_SHADOW_SNEAK,
                MOVE_WILL_O_WISP,
                MOVE_FLAME_CHARGE,
            },
            },
        },
    },
#line 3309
#line 3311
    [DIFFICULTY_EASY][TRAINER_ROUTE6_A] =
    {
#line 3310
        .trainerName = _("Owen"),
#line 3312
        .trainerClass = TRAINER_CLASS_PKMN_RANGER,
#line 3313
        .trainerPic = TRAINER_PIC_POKEMON_RANGER_M,
        .encounterMusic_gender =
#line 3315
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 3316
        .doubleBattle = FALSE,
#line 3317
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 3319
            .species = SPECIES_PALPITOAD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3321
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3320
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3323
#line 3325
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_A] =
    {
#line 3324
        .trainerName = _("Owen"),
#line 3326
        .trainerClass = TRAINER_CLASS_PKMN_RANGER,
#line 3327
        .trainerPic = TRAINER_PIC_POKEMON_RANGER_M,
        .encounterMusic_gender =
#line 3329
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 3331
        .items = { ITEM_LEMONADE },
#line 3330
        .doubleBattle = FALSE,
#line 3332
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 3334
            .species = SPECIES_PALPITOAD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3336
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3335
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3347
#line 3349
    [DIFFICULTY_EASY][TRAINER_ROUTE6_B] =
    {
#line 3348
        .trainerName = _("Puncher"),
#line 3350
        .trainerClass = TRAINER_CLASS_SAILOR,
#line 3351
        .trainerPic = TRAINER_PIC_SAILOR,
        .encounterMusic_gender =
#line 3353
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 3354
        .doubleBattle = FALSE,
#line 3355
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 3357
            .species = SPECIES_QWILFISH_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3359
            .iv = TRAINER_PARTY_IVS(13, 13, 13, 13, 13, 13),
#line 3358
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3361
#line 3363
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_B] =
    {
#line 3362
        .trainerName = _("Puncher"),
#line 3364
        .trainerClass = TRAINER_CLASS_SAILOR,
#line 3365
        .trainerPic = TRAINER_PIC_SAILOR,
        .encounterMusic_gender =
#line 3367
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 3368
        .doubleBattle = FALSE,
#line 3369
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 3371
            .species = SPECIES_QWILFISH_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3371
            .heldItem = ITEM_STICKY_BARB,
#line 3373
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3372
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3385
#line 3387
    [DIFFICULTY_EASY][TRAINER_ROUTE6_C] =
    {
#line 3386
        .trainerName = _("Sanya"),
#line 3388
        .trainerClass = TRAINER_CLASS_PKMN_RANGER,
#line 3389
        .trainerPic = TRAINER_PIC_POKEMON_RANGER_F,
        .encounterMusic_gender =
#line 3390
F_TRAINER_FEMALE | 
#line 3391
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 3392
        .doubleBattle = FALSE,
#line 3393
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 3395
            .species = SPECIES_SCYTHER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3397
            .iv = TRAINER_PARTY_IVS(14, 14, 14, 14, 14, 14),
#line 3396
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3400
#line 3402
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_C] =
    {
#line 3401
        .trainerName = _("Sanya"),
#line 3403
        .trainerClass = TRAINER_CLASS_PKMN_RANGER,
#line 3404
        .trainerPic = TRAINER_PIC_POKEMON_RANGER_F,
        .encounterMusic_gender =
#line 3405
F_TRAINER_FEMALE | 
#line 3406
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 3407
        .doubleBattle = FALSE,
#line 3408
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_FORCE_SETUP_FIRST_TURN,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 3410
            .species = SPECIES_SCIZOR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3410
            .heldItem = ITEM_METAL_COAT,
#line 3413
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3411
            .ability = ABILITY_TECHNICIAN,
#line 3412
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3413
                MOVE_SWORDS_DANCE,
                MOVE_BULLET_PUNCH,
            },
            },
        },
    },
#line 3422
#line 3424
    [DIFFICULTY_EASY][TRAINER_ROUTE6_D] =
    {
#line 3423
        .trainerName = _("Ahren"),
#line 3425
        .trainerClass = TRAINER_CLASS_FISHERMAN,
#line 3426
        .trainerPic = TRAINER_PIC_FISHERMAN,
        .encounterMusic_gender =
#line 3428
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 3429
        .doubleBattle = FALSE,
#line 3430
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3432
            .species = SPECIES_TOEDSCOOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3434
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 3433
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3436
            .species = SPECIES_MAREANIE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3438
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 3437
            .lvl = 27,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3440
#line 3442
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_D] =
    {
#line 3441
        .trainerName = _("Ahren"),
#line 3443
        .trainerClass = TRAINER_CLASS_FISHERMAN,
#line 3444
        .trainerPic = TRAINER_PIC_FISHERMAN,
        .encounterMusic_gender =
#line 3446
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 3447
        .doubleBattle = FALSE,
#line 3448
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3450
            .species = SPECIES_TOEDSCOOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3452
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3451
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3453
            .species = SPECIES_MAREANIE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3453
            .heldItem = ITEM_ROCKY_HELMET,
#line 3456
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3454
            .ability = ABILITY_ROUGH_SKIN,
#line 3455
            .lvl = 27,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3460
#line 3462
    [DIFFICULTY_EASY][TRAINER_ROUTE6_E] =
    {
#line 3461
        .trainerName = _("Koan"),
#line 3463
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 3464
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 3466
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 3467
        .items = { ITEM_SUPER_POTION },
#line 3468
        .doubleBattle = FALSE,
#line 3469
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 3471
            .species = SPECIES_CROCONAW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3473
            .iv = TRAINER_PARTY_IVS(17, 17, 17, 17, 17, 17),
#line 3472
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3475
#line 3477
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_E] =
    {
#line 3476
        .trainerName = _("Koan"),
#line 3478
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 3479
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 3481
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 3482
        .items = { ITEM_SUPER_POTION },
#line 3483
        .doubleBattle = FALSE,
#line 3484
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 3486
            .species = SPECIES_CROCONAW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3486
            .heldItem = ITEM_DARK_GEM,
#line 3488
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3487
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3488
                MOVE_CRUNCH,
                MOVE_WATERFALL,
            },
            },
        },
    },
#line 3500
#line 3502
    [DIFFICULTY_EASY][TRAINER_ROUTE6_F] =
    {
#line 3501
        .trainerName = _("Takao"),
#line 3503
        .trainerClass = TRAINER_CLASS_BLACK_BELT,
#line 3504
        .trainerPic = TRAINER_PIC_BLACK_BELT,
        .encounterMusic_gender =
#line 3506
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 3507
        .doubleBattle = FALSE,
#line 3508
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3510
            .species = SPECIES_CROAGUNK,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3512
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 3511
            .lvl = 27,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3514
            .species = SPECIES_CROAGUNK,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3516
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 3515
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3518
#line 3520
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_F] =
    {
#line 3519
        .trainerName = _("Takao"),
#line 3521
        .trainerClass = TRAINER_CLASS_BLACK_BELT,
#line 3522
        .trainerPic = TRAINER_PIC_BLACK_BELT,
        .encounterMusic_gender =
#line 3524
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 3525
        .doubleBattle = FALSE,
#line 3526
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3528
            .species = SPECIES_SNEASEL_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3528
            .heldItem = ITEM_RAZOR_FANG,
#line 3530
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3529
            .lvl = 27,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3531
            .species = SPECIES_CROAGUNK,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3531
            .heldItem = ITEM_EXPERT_BELT,
#line 3533
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3532
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3545
#line 3547
    [DIFFICULTY_EASY][TRAINER_ROUTE6_G] =
    {
#line 3546
        .trainerName = _("Adinya"),
#line 3548
        .trainerClass = TRAINER_CLASS_PKMN_BREEDER,
#line 3549
        .trainerPic = TRAINER_PIC_POKEMON_BREEDER_M,
        .encounterMusic_gender =
#line 3551
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 3552
        .doubleBattle = FALSE,
#line 3553
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
#line 3554
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 3556
            .species = SPECIES_MANECTRIC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3558
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 3557
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3560
            .species = SPECIES_HOUNDOOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3562
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 3561
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3564
            .species = SPECIES_LYCANROC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3566
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 3565
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3568
#line 3570
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_G] =
    {
#line 3569
        .trainerName = _("Adinya"),
#line 3571
        .trainerClass = TRAINER_CLASS_PKMN_BREEDER,
#line 3572
        .trainerPic = TRAINER_PIC_POKEMON_BREEDER_M,
        .encounterMusic_gender =
#line 3574
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 3576
        .items = { ITEM_SUPER_POTION },
#line 3575
        .doubleBattle = FALSE,
#line 3577
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
#line 3578
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 3580
            .species = SPECIES_MANECTRIC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3580
            .heldItem = ITEM_ORAN_BERRY,
#line 3582
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3581
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3583
            .species = SPECIES_HOUNDOOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3583
            .heldItem = ITEM_FIRE_GEM,
#line 3585
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3584
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3586
            .species = SPECIES_LYCANROC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3586
            .heldItem = ITEM_ROCK_GEM,
#line 3588
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3587
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3604
#line 3606
    [DIFFICULTY_EASY][TRAINER_ROUTE6_H] =
    {
#line 3605
        .trainerName = _("Briar"),
#line 3607
        .trainerClass = TRAINER_CLASS_BUG_CATCHER,
#line 3608
        .trainerPic = TRAINER_PIC_BUG_CATCHER,
        .encounterMusic_gender =
#line 3610
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 3611
        .doubleBattle = FALSE,
#line 3612
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 3614
            .species = SPECIES_SWADLOON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3616
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3615
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3618
            .species = SPECIES_DOTTLER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3620
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3619
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3622
            .species = SPECIES_WIMPOD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3624
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3623
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3626
#line 3628
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_H] =
    {
#line 3627
        .trainerName = _("Briar"),
#line 3629
        .trainerClass = TRAINER_CLASS_BUG_CATCHER,
#line 3630
        .trainerPic = TRAINER_PIC_BUG_CATCHER,
        .encounterMusic_gender =
#line 3632
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 3633
        .doubleBattle = FALSE,
#line 3634
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 3636
            .species = SPECIES_SWADLOON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3638
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3637
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3639
            .species = SPECIES_DOTTLER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3641
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3640
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3642
            .species = SPECIES_WIMPOD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3644
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3643
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3664
#line 3666
    [DIFFICULTY_EASY][TRAINER_ROUTE6_I] =
    {
#line 3665
        .trainerName = _("Nicolas"),
#line 3667
        .trainerClass = TRAINER_CLASS_DRAGON_TAMER,
#line 3668
        .trainerPic = TRAINER_PIC_DRAGON_TAMER,
        .encounterMusic_gender =
#line 3670
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 3671
        .doubleBattle = FALSE,
#line 3672
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3674
            .species = SPECIES_SWABLU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3676
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3675
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3678
            .species = SPECIES_SKRELP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3680
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3679
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3682
#line 3684
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_I] =
    {
#line 3683
        .trainerName = _("Nicolas"),
#line 3685
        .trainerClass = TRAINER_CLASS_DRAGON_TAMER,
#line 3686
        .trainerPic = TRAINER_PIC_DRAGON_TAMER,
        .encounterMusic_gender =
#line 3688
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 3689
        .doubleBattle = FALSE,
#line 3690
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3692
            .species = SPECIES_SWABLU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3692
            .heldItem = ITEM_ORAN_BERRY,
#line 3694
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3693
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3695
            .species = SPECIES_SKRELP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3697
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3696
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3711
#line 3713
    [DIFFICULTY_EASY][TRAINER_ROUTE6_J] =
    {
#line 3712
        .trainerName = _("Calvin"),
#line 3714
        .trainerClass = TRAINER_CLASS_YOUNGSTER,
#line 3715
        .trainerPic = TRAINER_PIC_YOUNGSTER,
        .encounterMusic_gender =
#line 3717
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 3718
        .doubleBattle = FALSE,
#line 3719
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3721
            .species = SPECIES_RATICATE_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3723
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3722
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3725
            .species = SPECIES_RUFFLET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3727
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3726
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3729
#line 3731
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_J] =
    {
#line 3730
        .trainerName = _("Calvin"),
#line 3732
        .trainerClass = TRAINER_CLASS_YOUNGSTER,
#line 3733
        .trainerPic = TRAINER_PIC_YOUNGSTER,
        .encounterMusic_gender =
#line 3735
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 3736
        .doubleBattle = FALSE,
#line 3737
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3739
            .species = SPECIES_RATICATE_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3741
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3740
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3742
            .species = SPECIES_RUFFLET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3744
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3743
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3762
#line 3764
    [DIFFICULTY_EASY][TRAINER_ROUTE6_K] =
    {
#line 3763
        .trainerName = _("Patricia"),
#line 3765
        .trainerClass = TRAINER_CLASS_HEX_MANIAC,
#line 3766
        .trainerPic = TRAINER_PIC_HEX_MANIAC,
        .encounterMusic_gender =
#line 3767
F_TRAINER_FEMALE | 
#line 3768
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 3769
        .doubleBattle = FALSE,
#line 3770
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3772
            .species = SPECIES_SHUPPET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3774
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3773
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3776
            .species = SPECIES_CURSOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3778
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3777
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3780
#line 3782
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_K] =
    {
#line 3781
        .trainerName = _("Patricia"),
#line 3783
        .trainerClass = TRAINER_CLASS_HEX_MANIAC,
#line 3784
        .trainerPic = TRAINER_PIC_HEX_MANIAC,
        .encounterMusic_gender =
#line 3785
F_TRAINER_FEMALE | 
#line 3786
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 3787
        .doubleBattle = FALSE,
#line 3788
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3790
            .species = SPECIES_SHUPPET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3792
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3791
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3793
            .species = SPECIES_CURSOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3795
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3794
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3808
#line 3810
    [DIFFICULTY_EASY][TRAINER_ROUTE6_GRUNT1] =
    {
#line 3809
        .trainerName = _("Brooke"),
#line 3811
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 3812
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 3813
F_TRAINER_FEMALE | 
#line 3814
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 3815
        .doubleBattle = TRUE,
#line 3816
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3818
            .species = SPECIES_GRIMER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3820
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3819
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3822
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3824
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3823
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3826
#line 3828
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_GRUNT1] =
    {
#line 3827
        .trainerName = _("Brooke"),
#line 3829
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 3830
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 3831
F_TRAINER_FEMALE | 
#line 3832
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 3833
        .doubleBattle = TRUE,
#line 3834
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3836
            .species = SPECIES_GRIMER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3838
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3837
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3839
            .species = SPECIES_DROWZEE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3841
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3840
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3842
#line 3844
    [DIFFICULTY_EASY][TRAINER_ROUTE6_GRUNT2] =
    {
#line 3843
        .trainerName = _("Hope"),
#line 3845
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 3846
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 3847
F_TRAINER_FEMALE | 
#line 3848
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 3849
        .doubleBattle = FALSE,
#line 3850
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3852
            .species = SPECIES_LOKIX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3854
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3853
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3856
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3858
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3857
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3860
#line 3862
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_GRUNT2] =
    {
#line 3861
        .trainerName = _("Hope"),
#line 3863
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 3864
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 3865
F_TRAINER_FEMALE | 
#line 3866
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 3867
        .doubleBattle = FALSE,
#line 3868
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 3870
            .species = SPECIES_LOKIX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3872
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3871
            .lvl = 28,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3873
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3875
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3874
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3888
#line 3890
    [DIFFICULTY_EASY][TRAINER_ROUTE6_GAB] =
    {
#line 3889
        .trainerName = _("Gabrielle"),
#line 3891
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 3892
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 3893
F_TRAINER_FEMALE | 
#line 3894
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 3895
        .items = { ITEM_FULL_RESTORE },
#line 3896
        .doubleBattle = FALSE,
#line 3897
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 3899
            .species = SPECIES_ZORUA_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3901
            .iv = TRAINER_PARTY_IVS(24, 24, 24, 24, 24, 24),
#line 3900
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3903
            .species = SPECIES_BALTOY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3905
            .iv = TRAINER_PARTY_IVS(24, 24, 24, 24, 24, 24),
#line 3904
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3907
            .species = SPECIES_MAWILE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3909
            .iv = TRAINER_PARTY_IVS(24, 24, 24, 24, 24, 24),
#line 3908
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3911
#line 3913
    [DIFFICULTY_NORMAL][TRAINER_ROUTE6_GAB] =
    {
#line 3912
        .trainerName = _("Gabrielle"),
#line 3914
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 3915
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 3916
F_TRAINER_FEMALE | 
#line 3917
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 3918
        .items = { ITEM_FULL_RESTORE },
#line 3919
        .doubleBattle = FALSE,
#line 3920
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 3922
            .species = SPECIES_ZORUA_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3924
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3923
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3925
            .species = SPECIES_BALTOY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3927
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3926
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3928
            .species = SPECIES_MAWILE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3930
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3929
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3941
#line 3943
    [DIFFICULTY_EASY][TRAINER_MIRROHBASECAMP_KOHLA] =
    {
#line 3942
        .trainerName = _("Kohla"),
#line 3944
        .trainerClass = TRAINER_CLASS_ACE_ROOKIE,
#line 3945
        .trainerPic = TRAINER_PIC_WALLY,
        .encounterMusic_gender =
#line 3947
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 3948
        .doubleBattle = FALSE,
#line 3949
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 3950
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 3952
            .species = SPECIES_SCYTHER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3954
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3953
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3956
            .species = SPECIES_DEWOTT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3958
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3957
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3960
            .species = SPECIES_GALLADE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3960
            .heldItem = ITEM_GALLADITE,
#line 3962
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3961
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3963
                MOVE_AERIAL_ACE,
                MOVE_PSYCHO_CUT,
                MOVE_DRAIN_PUNCH,
                MOVE_BULK_UP,
            },
            },
            {
#line 3968
            .species = SPECIES_CERULEDGE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3970
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 3969
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 3972
#line 3974
    [DIFFICULTY_NORMAL][TRAINER_MIRROHBASECAMP_KOHLA] =
    {
#line 3973
        .trainerName = _("Kohla"),
#line 3975
        .trainerClass = TRAINER_CLASS_ACE_ROOKIE,
#line 3976
        .trainerPic = TRAINER_PIC_WALLY,
        .encounterMusic_gender =
#line 3978
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 3979
        .doubleBattle = FALSE,
#line 3980
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 3981
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 3983
            .species = SPECIES_SCYTHER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3985
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3984
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3986
            .species = SPECIES_DEWOTT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3988
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3987
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 3989
            .species = SPECIES_GALLADE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3989
            .heldItem = ITEM_GALLADITE,
#line 3991
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3990
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 3991
                MOVE_AERIAL_ACE,
                MOVE_PSYCHO_CUT,
                MOVE_DRAIN_PUNCH,
                MOVE_BULK_UP,
            },
            },
            {
#line 3996
            .species = SPECIES_CERULEDGE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 3998
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 3997
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4007
#line 4009
    [DIFFICULTY_EASY][TRAINER_MIRROHBASECAMP_LEADER] =
    {
#line 4008
        .trainerName = _("Carona"),
#line 4010
        .trainerClass = TRAINER_CLASS_LEADER,
#line 4011
        .trainerPic = TRAINER_PIC_LEADER_CARONA,
        .encounterMusic_gender =
#line 4012
F_TRAINER_FEMALE | 
#line 4013
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 4014
        .items = { ITEM_FULL_RESTORE },
#line 4015
        .doubleBattle = FALSE,
#line 4016
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 4017
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 4019
            .species = SPECIES_TOXICROAK,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4021
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 4020
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4023
            .species = SPECIES_PANGORO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4025
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 4024
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4027
            .species = SPECIES_ANNIHILAPE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4029
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 4028
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4031
            .species = SPECIES_MEDICHAM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4031
            .heldItem = ITEM_MEDICHAMITE,
#line 4033
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 4032
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4035
#line 4037
    [DIFFICULTY_NORMAL][TRAINER_MIRROHBASECAMP_LEADER] =
    {
#line 4036
        .trainerName = _("Carona"),
#line 4038
        .trainerClass = TRAINER_CLASS_LEADER,
#line 4039
        .trainerPic = TRAINER_PIC_LEADER_CARONA,
        .encounterMusic_gender =
#line 4040
F_TRAINER_FEMALE | 
#line 4041
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 4042
        .items = { ITEM_FULL_RESTORE },
#line 4043
        .doubleBattle = FALSE,
#line 4044
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 4045
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 4047
            .species = SPECIES_SNEASLER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4047
            .heldItem = ITEM_FIGHTING_GEM,
#line 4050
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4048
            .ability = ABILITY_UNBURDEN,
#line 4049
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4050
                MOVE_DIRE_CLAW,
                MOVE_ACROBATICS,
                MOVE_CLOSE_COMBAT,
            },
            },
            {
#line 4054
            .species = SPECIES_PANGORO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4054
            .heldItem = ITEM_LEFTOVERS,
#line 4057
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4055
            .ability = ABILITY_IRON_FIST,
#line 4056
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4057
                MOVE_BULLET_PUNCH,
                MOVE_DRAIN_PUNCH,
                MOVE_POWER_UP_PUNCH,
                MOVE_THUNDER_PUNCH,
            },
            },
            {
#line 4062
            .species = SPECIES_ANNIHILAPE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4062
            .heldItem = ITEM_LIFE_ORB,
#line 4065
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4063
            .ability = ABILITY_DEFIANT,
#line 4064
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4065
                MOVE_RAGE_FIST,
                MOVE_BULK_UP,
                MOVE_DRAIN_PUNCH,
                MOVE_ROCK_SLIDE,
            },
            },
            {
#line 4070
            .species = SPECIES_MEDICHAM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4070
            .heldItem = ITEM_MEDICHAMITE,
#line 4072
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4071
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4072
                MOVE_HI_JUMP_KICK,
                MOVE_PSYCHO_CUT,
            },
            },
        },
    },
#line 4091
#line 4093
    [DIFFICULTY_EASY][TRAINER_MIRROHEXT_A] =
    {
#line 4092
        .trainerName = _("Sentry"),
#line 4094
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 4095
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 4096
F_TRAINER_FEMALE | 
#line 4097
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 4098
        .items = { ITEM_HYPER_POTION },
#line 4099
        .doubleBattle = FALSE,
#line 4100
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 4102
            .species = SPECIES_PALPITOAD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4105
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 4103
            .ability = ABILITY_WATER_ABSORB,
#line 4104
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4106
                MOVE_BUBBLEBEAM,
                MOVE_FLAIL,
                MOVE_MUD_SHOT,
                MOVE_UPROAR,
            },
            },
            {
#line 4111
            .species = SPECIES_QUILAVA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4113
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 4112
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4114
                MOVE_SWIFT,
                MOVE_FIRE_SPIN,
                MOVE_SMOKESCREEN,
                MOVE_ENDURE,
            },
            },
            {
#line 4119
            .species = SPECIES_LAIRON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4122
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 4121
            .ability = ABILITY_ROCK_HEAD,
#line 4120
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4123
                MOVE_PROTECT,
                MOVE_IRON_HEAD,
                MOVE_ROCK_SLIDE,
                MOVE_TAKE_DOWN,
            },
            },
        },
    },
#line 4128
#line 4130
    [DIFFICULTY_NORMAL][TRAINER_MIRROHEXT_A] =
    {
#line 4129
        .trainerName = _("Sentry"),
#line 4131
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 4132
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 4133
F_TRAINER_FEMALE | 
#line 4134
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 4135
        .items = { ITEM_HYPER_POTION },
#line 4136
        .doubleBattle = FALSE,
#line 4137
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 4139
            .species = SPECIES_PALPITOAD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4142
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4140
            .ability = ABILITY_WATER_ABSORB,
#line 4141
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4142
                MOVE_BUBBLEBEAM,
                MOVE_FLAIL,
                MOVE_MUD_SHOT,
                MOVE_UPROAR,
            },
            },
            {
#line 4147
            .species = SPECIES_QUILAVA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4149
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4148
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4149
                MOVE_SWIFT,
                MOVE_FIRE_SPIN,
                MOVE_SMOKESCREEN,
                MOVE_ENDURE,
            },
            },
            {
#line 4154
            .species = SPECIES_LAIRON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4157
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4156
            .ability = ABILITY_ROCK_HEAD,
#line 4155
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4157
                MOVE_PROTECT,
                MOVE_IRON_HEAD,
                MOVE_ROCK_SLIDE,
                MOVE_TAKE_DOWN,
            },
            },
        },
    },
#line 4180
#line 4182
    [DIFFICULTY_EASY][TRAINER_MIRROHEXT_B] =
    {
#line 4181
        .trainerName = _("Badshah"),
#line 4183
        .trainerClass = TRAINER_CLASS_NINJA_BOY,
#line 4184
        .trainerPic = TRAINER_PIC_NINJA_BOY,
        .encounterMusic_gender =
#line 4186
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4187
        .doubleBattle = FALSE,
#line 4188
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE | AI_FLAG_TRY_TO_FAINT,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4190
            .species = SPECIES_VIVILLON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4192
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 4191
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4194
            .species = SPECIES_SNOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4196
            .iv = TRAINER_PARTY_IVS(13, 13, 13, 13, 13, 13),
#line 4195
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4198
#line 4200
    [DIFFICULTY_NORMAL][TRAINER_MIRROHEXT_B] =
    {
#line 4199
        .trainerName = _("Badshah"),
#line 4201
        .trainerClass = TRAINER_CLASS_NINJA_BOY,
#line 4202
        .trainerPic = TRAINER_PIC_NINJA_BOY,
        .encounterMusic_gender =
#line 4204
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4205
        .doubleBattle = FALSE,
#line 4206
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4208
            .species = SPECIES_VIVILLON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4210
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4209
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4211
            .species = SPECIES_SNOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4213
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4212
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4227
#line 4229
    [DIFFICULTY_EASY][TRAINER_MIRROHEXT_C] =
    {
#line 4228
        .trainerName = _("Bianca"),
#line 4230
        .trainerClass = TRAINER_CLASS_SKIIER,
#line 4231
        .trainerPic = TRAINER_PIC_SKIIER_F,
        .encounterMusic_gender =
#line 4232
F_TRAINER_FEMALE | 
#line 4233
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 4234
        .doubleBattle = FALSE,
#line 4235
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4237
            .species = SPECIES_MEOWTH_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4239
            .iv = TRAINER_PARTY_IVS(14, 14, 14, 14, 14, 14),
#line 4238
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4241
            .species = SPECIES_SANDSHREW_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4243
            .iv = TRAINER_PARTY_IVS(14, 14, 14, 14, 14, 14),
#line 4242
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4245
#line 4247
    [DIFFICULTY_NORMAL][TRAINER_MIRROHEXT_C] =
    {
#line 4246
        .trainerName = _("Bianca"),
#line 4248
        .trainerClass = TRAINER_CLASS_SKIIER,
#line 4249
        .trainerPic = TRAINER_PIC_SKIIER_F,
        .encounterMusic_gender =
#line 4250
F_TRAINER_FEMALE | 
#line 4251
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 4252
        .doubleBattle = FALSE,
#line 4253
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4255
            .species = SPECIES_MEOWTH_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4257
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4256
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4258
            .species = SPECIES_SANDSHREW_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4260
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4259
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4275
#line 4277
    [DIFFICULTY_EASY][TRAINER_MIRROHEXT_D] =
    {
#line 4276
        .trainerName = _("Bianca"),
#line 4278
        .trainerClass = TRAINER_CLASS_PKMN_BREEDER,
#line 4279
        .trainerPic = TRAINER_PIC_POKEMON_BREEDER_F,
        .encounterMusic_gender =
#line 4281
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 4282
        .doubleBattle = FALSE,
#line 4283
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4285
            .species = SPECIES_STANTLER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4287
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 4286
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4289
            .species = SPECIES_RAPIDASH_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4291
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 4290
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4293
#line 4295
    [DIFFICULTY_NORMAL][TRAINER_MIRROHEXT_D] =
    {
#line 4294
        .trainerName = _("Bianca"),
#line 4296
        .trainerClass = TRAINER_CLASS_PKMN_BREEDER,
#line 4297
        .trainerPic = TRAINER_PIC_POKEMON_BREEDER_F,
        .encounterMusic_gender =
#line 4299
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 4300
        .doubleBattle = FALSE,
#line 4301
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4303
            .species = SPECIES_STANTLER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4305
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4304
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4306
            .species = SPECIES_RAPIDASH_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4308
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4307
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4321
#line 4323
    [DIFFICULTY_EASY][TRAINER_MIRROHEXT_E] =
    {
#line 4322
        .trainerName = _("Junipurr"),
#line 4324
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 4325
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 4326
F_TRAINER_FEMALE | 
#line 4327
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 4328
        .doubleBattle = FALSE,
#line 4329
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 4331
            .species = SPECIES_DREEPY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4334
            .iv = TRAINER_PARTY_IVS(17, 17, 17, 17, 17, 17),
#line 4332
            .ability = ABILITY_INFILTRATOR,
#line 4333
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4335
                MOVE_DRAGON_TAIL,
                MOVE_SUCKER_PUNCH,
                MOVE_QUICK_ATTACK,
                MOVE_FACADE,
            },
            },
            {
#line 4340
            .species = SPECIES_TINKATUFF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4344
            .iv = TRAINER_PARTY_IVS(17, 17, 17, 17, 17, 17),
#line 4343
            .ability = ABILITY_MOLD_BREAKER,
#line 4341
            .lvl = 30,
#line 4342
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4345
                MOVE_PLAY_ROUGH,
                MOVE_FLASH_CANNON,
                MOVE_ICE_HAMMER,
                MOVE_FOUL_PLAY,
            },
            },
            {
#line 4350
            .species = SPECIES_BRAIXEN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4354
            .iv = TRAINER_PARTY_IVS(17, 17, 17, 17, 17, 17),
#line 4353
            .ability = ABILITY_BLAZE,
#line 4351
            .lvl = 32,
#line 4352
            .nature = NATURE_TIMID,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4355
                MOVE_FLAMETHROWER,
                MOVE_WILL_O_WISP,
                MOVE_SUNNY_DAY,
                MOVE_GRASS_KNOT,
            },
            },
        },
    },
#line 4360
#line 4362
    [DIFFICULTY_NORMAL][TRAINER_MIRROHEXT_E] =
    {
#line 4361
        .trainerName = _("Junipurr"),
#line 4363
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 4364
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 4365
F_TRAINER_FEMALE | 
#line 4366
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 4367
        .doubleBattle = FALSE,
#line 4368
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 4370
            .species = SPECIES_DREEPY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4373
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4371
            .ability = ABILITY_INFILTRATOR,
#line 4372
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4373
                MOVE_DRAGON_TAIL,
                MOVE_SUCKER_PUNCH,
                MOVE_QUICK_ATTACK,
                MOVE_FACADE,
            },
            },
            {
#line 4378
            .species = SPECIES_TINKATUFF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4382
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4381
            .ability = ABILITY_MOLD_BREAKER,
#line 4379
            .lvl = 30,
#line 4380
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4382
                MOVE_PLAY_ROUGH,
                MOVE_FLASH_CANNON,
                MOVE_ICE_HAMMER,
                MOVE_FOUL_PLAY,
            },
            },
            {
#line 4387
            .species = SPECIES_BRAIXEN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4391
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4390
            .ability = ABILITY_BLAZE,
#line 4388
            .lvl = 32,
#line 4389
            .nature = NATURE_TIMID,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4391
                MOVE_FLAMETHROWER,
                MOVE_WILL_O_WISP,
                MOVE_SUNNY_DAY,
                MOVE_GRASS_KNOT,
            },
            },
        },
    },
#line 4409
#line 4411
    [DIFFICULTY_EASY][TRAINER_MIRROHEXT_F] =
    {
#line 4410
        .trainerName = _("Ringer"),
#line 4412
        .trainerClass = TRAINER_CLASS_GUITARIST,
#line 4413
        .trainerPic = TRAINER_PIC_GUITARIST,
        .encounterMusic_gender =
#line 4415
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4416
        .doubleBattle = FALSE,
#line 4417
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 4419
            .species = SPECIES_BANETTE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4421
            .iv = TRAINER_PARTY_IVS(17, 17, 17, 17, 17, 17),
#line 4420
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4423
#line 4425
    [DIFFICULTY_NORMAL][TRAINER_MIRROHEXT_F] =
    {
#line 4424
        .trainerName = _("Ringer"),
#line 4426
        .trainerClass = TRAINER_CLASS_GUITARIST,
#line 4427
        .trainerPic = TRAINER_PIC_GUITARIST,
        .encounterMusic_gender =
#line 4429
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4430
        .doubleBattle = FALSE,
#line 4431
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 4433
            .species = SPECIES_BANETTE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4435
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4434
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4450
#line 4452
    [DIFFICULTY_EASY][TRAINER_MIRROHEXT_G] =
    {
#line 4451
        .trainerName = _("Kindra"),
#line 4453
        .trainerClass = TRAINER_CLASS_BLACK_BELT,
#line 4454
        .trainerPic = TRAINER_PIC_BLACK_BELT,
        .encounterMusic_gender =
#line 4455
F_TRAINER_FEMALE | 
#line 4456
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4457
        .doubleBattle = FALSE,
#line 4458
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4460
            .species = SPECIES_PANCHAM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4462
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 4461
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4464
            .species = SPECIES_PASSIMIAN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4466
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 4465
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4468
#line 4470
    [DIFFICULTY_NORMAL][TRAINER_MIRROHEXT_G] =
    {
#line 4469
        .trainerName = _("Kindra"),
#line 4471
        .trainerClass = TRAINER_CLASS_BLACK_BELT,
#line 4472
        .trainerPic = TRAINER_PIC_BLACK_BELT,
        .encounterMusic_gender =
#line 4473
F_TRAINER_FEMALE | 
#line 4474
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4475
        .doubleBattle = FALSE,
#line 4476
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4478
            .species = SPECIES_PANCHAM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4480
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4479
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4481
            .species = SPECIES_PASSIMIAN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4483
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4482
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4484
#line 4486
    [DIFFICULTY_EASY][TRAINER_MIRROHEXT_H] =
    {
#line 4485
        .trainerName = _("Tammy"),
#line 4487
        .trainerClass = TRAINER_CLASS_BATTLE_GIRL,
#line 4488
        .trainerPic = TRAINER_PIC_BATTLE_GIRL,
        .encounterMusic_gender =
#line 4489
F_TRAINER_FEMALE | 
#line 4490
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4491
        .doubleBattle = FALSE,
#line 4492
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4494
            .species = SPECIES_GURDURR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4496
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 4495
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4498
            .species = SPECIES_PRIMEAPE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4500
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 4499
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4502
#line 4504
    [DIFFICULTY_NORMAL][TRAINER_MIRROHEXT_H] =
    {
#line 4503
        .trainerName = _("Tammy"),
#line 4505
        .trainerClass = TRAINER_CLASS_BATTLE_GIRL,
#line 4506
        .trainerPic = TRAINER_PIC_BATTLE_GIRL,
        .encounterMusic_gender =
#line 4507
F_TRAINER_FEMALE | 
#line 4508
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4509
        .doubleBattle = FALSE,
#line 4510
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4512
            .species = SPECIES_GURDURR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4514
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4513
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4515
            .species = SPECIES_PRIMEAPE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4517
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4516
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4529
#line 4531
    [DIFFICULTY_EASY][TRAINER_MIRROHINT_A] =
    {
#line 4530
        .trainerName = _("Elo"),
#line 4532
        .trainerClass = TRAINER_CLASS_HIKER,
#line 4533
        .trainerPic = TRAINER_PIC_HIKER,
        .encounterMusic_gender =
#line 4535
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 4536
        .doubleBattle = FALSE,
#line 4537
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4539
            .species = SPECIES_CETODDLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4541
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 4540
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4543
            .species = SPECIES_GRAVELER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4545
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 4544
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4547
#line 4549
    [DIFFICULTY_NORMAL][TRAINER_MIRROHINT_A] =
    {
#line 4548
        .trainerName = _("Elo"),
#line 4550
        .trainerClass = TRAINER_CLASS_HIKER,
#line 4551
        .trainerPic = TRAINER_PIC_HIKER,
        .encounterMusic_gender =
#line 4553
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 4554
        .doubleBattle = FALSE,
#line 4555
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4557
            .species = SPECIES_CETODDLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4559
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4558
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4560
            .species = SPECIES_GRAVELER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4562
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4561
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4574
#line 4576
    [DIFFICULTY_EASY][TRAINER_MIRROHINT_B] =
    {
#line 4575
        .trainerName = _("Wyatt"),
#line 4577
        .trainerClass = TRAINER_CLASS_POKEMANIAC,
#line 4578
        .trainerPic = TRAINER_PIC_POKEMANIAC,
        .encounterMusic_gender =
#line 4580
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4581
        .doubleBattle = FALSE,
#line 4582
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4584
            .species = SPECIES_SHUPPET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4586
            .iv = TRAINER_PARTY_IVS(6, 6, 6, 6, 6, 6),
#line 4585
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4588
            .species = SPECIES_SINISTCHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4590
            .iv = TRAINER_PARTY_IVS(6, 6, 6, 6, 6, 6),
#line 4589
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4592
#line 4594
    [DIFFICULTY_NORMAL][TRAINER_MIRROHINT_B] =
    {
#line 4593
        .trainerName = _("Wyatt"),
#line 4595
        .trainerClass = TRAINER_CLASS_POKEMANIAC,
#line 4596
        .trainerPic = TRAINER_PIC_POKEMANIAC,
        .encounterMusic_gender =
#line 4598
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4599
        .doubleBattle = FALSE,
#line 4600
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4602
            .species = SPECIES_SHUPPET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4604
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4603
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4605
            .species = SPECIES_SINISTCHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4607
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4606
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4620
#line 4622
    [DIFFICULTY_EASY][TRAINER_MIRROHINT_C] =
    {
#line 4621
        .trainerName = _("Verdun"),
#line 4623
        .trainerClass = TRAINER_CLASS_HIKER,
#line 4624
        .trainerPic = TRAINER_PIC_HIKER,
        .encounterMusic_gender =
#line 4626
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 4627
        .doubleBattle = FALSE,
#line 4628
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 4630
            .species = SPECIES_BERGMITE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4632
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 4631
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4634
#line 4636
    [DIFFICULTY_NORMAL][TRAINER_MIRROHINT_C] =
    {
#line 4635
        .trainerName = _("Verdun"),
#line 4637
        .trainerClass = TRAINER_CLASS_HIKER,
#line 4638
        .trainerPic = TRAINER_PIC_HIKER,
        .encounterMusic_gender =
#line 4640
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 4641
        .doubleBattle = FALSE,
#line 4642
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 4644
            .species = SPECIES_BERGMITE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4646
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4645
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4657
#line 4659
    [DIFFICULTY_EASY][TRAINER_MIRROHINT_D] =
    {
#line 4658
        .trainerName = _("Friston"),
#line 4660
        .trainerClass = TRAINER_CLASS_BURGLAR,
#line 4661
        .trainerPic = TRAINER_PIC_BURGLAR,
        .encounterMusic_gender =
#line 4663
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 4664
        .doubleBattle = FALSE,
#line 4665
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 4667
            .species = SPECIES_NICKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4669
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 4668
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4671
            .species = SPECIES_THIEVUL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4673
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 4672
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4675
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4677
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 4676
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4679
#line 4681
    [DIFFICULTY_NORMAL][TRAINER_MIRROHINT_D] =
    {
#line 4680
        .trainerName = _("Friston"),
#line 4682
        .trainerClass = TRAINER_CLASS_BURGLAR,
#line 4683
        .trainerPic = TRAINER_PIC_BURGLAR,
        .encounterMusic_gender =
#line 4685
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 4686
        .doubleBattle = FALSE,
#line 4687
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 4689
            .species = SPECIES_THIEVUL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4691
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4690
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4692
            .species = SPECIES_THIEVUL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4694
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4693
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4695
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4697
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4696
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4716
#line 4718
    [DIFFICULTY_EASY][TRAINER_MIRROHINT_E] =
    {
#line 4717
        .trainerName = _("Duo"),
#line 4719
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 4720
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_DUO,
        .encounterMusic_gender =
#line 4722
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4723
        .doubleBattle = TRUE,
#line 4724
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4726
            .species = SPECIES_GRIMER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4728
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 4727
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4730
            .species = SPECIES_MIME_JR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4732
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 4731
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4734
#line 4736
    [DIFFICULTY_NORMAL][TRAINER_MIRROHINT_E] =
    {
#line 4735
        .trainerName = _("Duo"),
#line 4737
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 4738
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_DUO,
        .encounterMusic_gender =
#line 4740
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4741
        .doubleBattle = TRUE,
#line 4742
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4744
            .species = SPECIES_GRIMER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4746
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4745
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4747
            .species = SPECIES_MIME_JR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4749
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4748
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4764
#line 4766
    [DIFFICULTY_EASY][TRAINER_MIRROHINT_F] =
    {
#line 4765
        .trainerName = _("VALERIE"),
#line 4767
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 4768
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 4770
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4771
        .doubleBattle = FALSE,
#line 4772
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 4774
            .species = SPECIES_DUSKULL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4776
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4775
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4778
#line 4780
    [DIFFICULTY_EASY][TRAINER_MIRROHINT2_A] =
    {
#line 4779
        .trainerName = _("Rein"),
#line 4781
        .trainerClass = TRAINER_CLASS_PSYCHIC,
#line 4782
        .trainerPic = TRAINER_PIC_PSYCHIC_M,
        .encounterMusic_gender =
#line 4784
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4785
        .doubleBattle = FALSE,
#line 4786
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4788
            .species = SPECIES_PONYTA_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4791
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 4790
            .ability = ABILITY_PASTEL_VEIL,
#line 4789
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4792
                MOVE_WILL_O_WISP,
                MOVE_STOMP,
                MOVE_PSYBEAM,
                MOVE_MORNING_SUN,
            },
            },
            {
#line 4797
            .species = SPECIES_WYRDEER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4799
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 4798
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4801
#line 4803
    [DIFFICULTY_NORMAL][TRAINER_MIRROHINT2_A] =
    {
#line 4802
        .trainerName = _("Rein"),
#line 4804
        .trainerClass = TRAINER_CLASS_PSYCHIC,
#line 4805
        .trainerPic = TRAINER_PIC_PSYCHIC_M,
        .encounterMusic_gender =
#line 4807
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4808
        .doubleBattle = FALSE,
#line 4809
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4811
            .species = SPECIES_PONYTA_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4814
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4813
            .ability = ABILITY_PASTEL_VEIL,
#line 4812
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 4814
                MOVE_WILL_O_WISP,
                MOVE_STOMP,
                MOVE_PSYBEAM,
                MOVE_MORNING_SUN,
            },
            },
            {
#line 4819
            .species = SPECIES_WYRDEER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4821
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4820
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4838
#line 4840
    [DIFFICULTY_EASY][TRAINER_MIRROHINT2_B] =
    {
#line 4839
        .trainerName = _("Shin"),
#line 4841
        .trainerClass = TRAINER_CLASS_POKEMANIAC,
#line 4842
        .trainerPic = TRAINER_PIC_POKEMANIAC,
        .encounterMusic_gender =
#line 4844
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4845
        .doubleBattle = FALSE,
#line 4846
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4848
            .species = SPECIES_PILOSWINE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4850
            .iv = TRAINER_PARTY_IVS(18, 18, 18, 18, 18, 18),
#line 4849
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4852
            .species = SPECIES_CARKOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4854
            .iv = TRAINER_PARTY_IVS(18, 18, 18, 18, 18, 18),
#line 4853
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4856
#line 4858
    [DIFFICULTY_NORMAL][TRAINER_MIRROHINT2_B] =
    {
#line 4857
        .trainerName = _("Shin"),
#line 4859
        .trainerClass = TRAINER_CLASS_POKEMANIAC,
#line 4860
        .trainerPic = TRAINER_PIC_POKEMANIAC,
        .encounterMusic_gender =
#line 4862
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 4863
        .doubleBattle = FALSE,
#line 4864
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4866
            .species = SPECIES_PILOSWINE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4868
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4867
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4869
            .species = SPECIES_CARKOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4871
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4870
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4884
#line 4886
    [DIFFICULTY_EASY][TRAINER_MIRROHINT2_C] =
    {
#line 4885
        .trainerName = _("Elona"),
#line 4887
        .trainerClass = TRAINER_CLASS_TRIATHLETE,
#line 4888
        .trainerPic = TRAINER_PIC_RUNNING_TRIATHLETE_F,
        .encounterMusic_gender =
#line 4889
F_TRAINER_FEMALE | 
#line 4890
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 4891
        .doubleBattle = FALSE,
#line 4892
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4894
            .species = SPECIES_VOLTORB_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4894
            .heldItem = ITEM_WIDE_LENS,
#line 4896
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 4895
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4898
            .species = SPECIES_LYCANROC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4900
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 30, 12, 12),
#line 4899
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4902
#line 4904
    [DIFFICULTY_NORMAL][TRAINER_MIRROHINT2_C] =
    {
#line 4903
        .trainerName = _("Elona"),
#line 4905
        .trainerClass = TRAINER_CLASS_TRIATHLETE,
#line 4906
        .trainerPic = TRAINER_PIC_RUNNING_TRIATHLETE_F,
        .encounterMusic_gender =
#line 4907
F_TRAINER_FEMALE | 
#line 4908
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 4909
        .doubleBattle = FALSE,
#line 4910
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4912
            .species = SPECIES_VOLTORB_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4912
            .heldItem = ITEM_WIDE_LENS,
#line 4914
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4913
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4915
            .species = SPECIES_LYCANROC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4917
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4916
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4920
#line 4922
    [DIFFICULTY_EASY][TRAINER_MIRROHINT2_D] =
    {
#line 4921
        .trainerName = _("Araya"),
#line 4923
        .trainerClass = TRAINER_CLASS_SKIIER,
#line 4924
        .trainerPic = TRAINER_PIC_SKIIER_F,
        .encounterMusic_gender =
#line 4925
F_TRAINER_FEMALE | 
#line 4926
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 4927
        .doubleBattle = FALSE,
#line 4928
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4930
            .species = SPECIES_MEOWTH_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4932
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 4931
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4934
            .species = SPECIES_SANDSLASH_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4936
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 4935
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4938
#line 4940
    [DIFFICULTY_NORMAL][TRAINER_MIRROHINT2_D] =
    {
#line 4939
        .trainerName = _("Araya"),
#line 4941
        .trainerClass = TRAINER_CLASS_SKIIER,
#line 4942
        .trainerPic = TRAINER_PIC_SKIIER_F,
        .encounterMusic_gender =
#line 4943
F_TRAINER_FEMALE | 
#line 4944
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 4945
        .doubleBattle = FALSE,
#line 4946
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 4948
            .species = SPECIES_MEOWTH_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4950
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4949
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4951
            .species = SPECIES_SANDSLASH_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4953
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 4952
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4967
#line 4969
    [DIFFICULTY_EASY][TRAINER_MIRROHINT2_E] =
    {
#line 4968
        .trainerName = _("Chara"),
#line 4970
        .trainerClass = TRAINER_CLASS_COOL_GIRL,
#line 4971
        .trainerPic = TRAINER_PIC_COOL_GIRL,
        .encounterMusic_gender =
#line 4972
F_TRAINER_FEMALE | 
#line 4973
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 4974
        .doubleBattle = FALSE,
#line 4975
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 4977
            .species = SPECIES_PINECO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4979
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 4978
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4981
            .species = SPECIES_URSARING,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4983
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 4982
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 4985
            .species = SPECIES_ALTARIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 4987
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 4986
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 4989
#line 4991
    [DIFFICULTY_NORMAL][TRAINER_MIRROHINT2_E] =
    {
#line 4990
        .trainerName = _("Chara"),
#line 4992
        .trainerClass = TRAINER_CLASS_COOL_GIRL,
#line 4993
        .trainerPic = TRAINER_PIC_COOL_GIRL,
        .encounterMusic_gender =
#line 4994
F_TRAINER_FEMALE | 
#line 4995
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 4996
        .doubleBattle = FALSE,
#line 4997
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 4999
            .species = SPECIES_PINECO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5001
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5000
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5002
            .species = SPECIES_URSARING,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5004
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5003
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5005
            .species = SPECIES_ALTARIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5007
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5006
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5020
#line 5022
    [DIFFICULTY_EASY][TRAINER_MIRROHINT2_F] =
    {
#line 5021
        .trainerName = _("VICTOR"),
#line 5023
        .trainerClass = TRAINER_CLASS_POKEFAN,
#line 5024
        .trainerPic = TRAINER_PIC_POKEFAN_M,
        .encounterMusic_gender =
#line 5026
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5027
        .doubleBattle = FALSE,
#line 5028
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 5030
            .species = SPECIES_CETODDLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5032
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 5031
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5034
            .species = SPECIES_FRIGIBAX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5036
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 5035
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5038
#line 5040
    [DIFFICULTY_NORMAL][TRAINER_MIRROHINT2_F] =
    {
#line 5039
        .trainerName = _("VICTOR"),
#line 5041
        .trainerClass = TRAINER_CLASS_POKEFAN,
#line 5042
        .trainerPic = TRAINER_PIC_POKEFAN_M,
        .encounterMusic_gender =
#line 5044
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5045
        .doubleBattle = FALSE,
#line 5046
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 5048
            .species = SPECIES_CETODDLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5050
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5049
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5051
            .species = SPECIES_FRIGIBAX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5053
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5052
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5067
#line 5069
    [DIFFICULTY_EASY][TRAINER_MIRROHINT2_G] =
    {
#line 5068
        .trainerName = _("Calvin"),
#line 5070
        .trainerClass = TRAINER_CLASS_YOUNGSTER,
#line 5071
        .trainerPic = TRAINER_PIC_YOUNGSTER,
        .encounterMusic_gender =
#line 5073
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5074
        .doubleBattle = FALSE,
#line 5075
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
#line 5076
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 5078
            .species = SPECIES_HERDIER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5080
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 5079
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5082
            .species = SPECIES_CORVISQUIRE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5084
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 5083
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5086
            .species = SPECIES_RATICATE_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5088
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 5087
            .lvl = 35,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5090
            .species = SPECIES_MAROWAK_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5092
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 5091
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5094
#line 5096
    [DIFFICULTY_NORMAL][TRAINER_MIRROHINT2_G] =
    {
#line 5095
        .trainerName = _("Calvin"),
#line 5097
        .trainerClass = TRAINER_CLASS_YOUNGSTER,
#line 5098
        .trainerPic = TRAINER_PIC_YOUNGSTER,
        .encounterMusic_gender =
#line 5100
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5101
        .doubleBattle = FALSE,
#line 5102
        .aiFlags = AI_FLAG_SMART_TRAINER,
#line 5103
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 5105
            .species = SPECIES_HERDIER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5107
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5106
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5108
            .species = SPECIES_CORVISQUIRE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5110
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5109
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5111
            .species = SPECIES_RATICATE_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5113
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5112
            .lvl = 35,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5114
            .species = SPECIES_MAROWAK_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5116
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5115
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5134
#line 5136
    [DIFFICULTY_EASY][TRAINER_MIRROHPEAK_A] =
    {
#line 5135
        .trainerName = _("Cindy"),
#line 5137
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 5138
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 5139
F_TRAINER_FEMALE | 
#line 5140
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 5141
        .items = { ITEM_FULL_RESTORE },
#line 5142
        .doubleBattle = FALSE,
#line 5143
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5145
            .species = SPECIES_YANMEGA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5147
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 5146
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5149
#line 5151
    [DIFFICULTY_NORMAL][TRAINER_MIRROHPEAK_A] =
    {
#line 5150
        .trainerName = _("Cindy"),
#line 5152
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 5153
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 5154
F_TRAINER_FEMALE | 
#line 5155
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 5156
        .items = { ITEM_FULL_RESTORE },
#line 5157
        .doubleBattle = FALSE,
#line 5158
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5160
            .species = SPECIES_YANMEGA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5162
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5161
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5176
#line 5178
    [DIFFICULTY_EASY][TRAINER_MIRROHPEAK_B] =
    {
#line 5177
        .trainerName = _("Jan"),
#line 5179
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 5180
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 5181
F_TRAINER_FEMALE | 
#line 5182
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 5183
        .items = { ITEM_FULL_RESTORE },
#line 5184
        .doubleBattle = FALSE,
#line 5185
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5187
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5189
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 5188
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5191
#line 5193
    [DIFFICULTY_NORMAL][TRAINER_MIRROHPEAK_B] =
    {
#line 5192
        .trainerName = _("Jan"),
#line 5194
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 5195
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 5196
F_TRAINER_FEMALE | 
#line 5197
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 5198
        .items = { ITEM_FULL_RESTORE },
#line 5199
        .doubleBattle = FALSE,
#line 5200
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5202
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5204
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5203
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5218
#line 5220
    [DIFFICULTY_EASY][TRAINER_MIRROHPEAK_C] =
    {
#line 5219
        .trainerName = _("Grunt"),
#line 5221
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 5222
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 5224
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5225
        .doubleBattle = FALSE,
#line 5226
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5228
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5230
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 5229
            .lvl = 35,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5232
#line 5234
    [DIFFICULTY_NORMAL][TRAINER_MIRROHPEAK_C] =
    {
#line 5233
        .trainerName = _("Grunt"),
#line 5235
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 5236
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 5238
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5239
        .doubleBattle = FALSE,
#line 5240
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5242
            .species = SPECIES_MURKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5244
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5243
            .lvl = 35,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5261
#line 5263
    [DIFFICULTY_EASY][TRAINER_MIRROHPEAK_D] =
    {
#line 5262
        .trainerName = _("Grunt"),
#line 5264
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 5265
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 5266
F_TRAINER_FEMALE | 
#line 5267
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 5268
        .doubleBattle = FALSE,
#line 5269
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5271
            .species = SPECIES_BRONZONG,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5273
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 5272
            .lvl = 35,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5275
#line 5277
    [DIFFICULTY_NORMAL][TRAINER_MIRROHPEAK_D] =
    {
#line 5276
        .trainerName = _("Grunt"),
#line 5278
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 5279
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 5280
F_TRAINER_FEMALE | 
#line 5281
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 5282
        .doubleBattle = FALSE,
#line 5283
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5285
            .species = SPECIES_BRONZONG,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5287
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5286
            .lvl = 35,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5301
#line 5303
    [DIFFICULTY_EASY][TRAINER_MIRROHPEAK_E] =
    {
#line 5302
        .trainerName = _("SHEILA"),
#line 5304
        .trainerClass = TRAINER_CLASS_BEAUTY,
#line 5305
        .trainerPic = TRAINER_PIC_BEAUTY,
        .encounterMusic_gender =
#line 5306
F_TRAINER_FEMALE | 
#line 5307
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 5308
        .doubleBattle = FALSE,
#line 5309
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5311
            .species = SPECIES_SHROOMISH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5313
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 5312
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5315
#line 5317
    [DIFFICULTY_NORMAL][TRAINER_MIRROHPEAK_E] =
    {
#line 5316
        .trainerName = _("SHEILA"),
#line 5318
        .trainerClass = TRAINER_CLASS_BEAUTY,
#line 5319
        .trainerPic = TRAINER_PIC_BEAUTY,
        .encounterMusic_gender =
#line 5320
F_TRAINER_FEMALE | 
#line 5321
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 5322
        .doubleBattle = FALSE,
#line 5323
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5325
            .species = SPECIES_SHROOMISH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5327
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5326
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5340
#line 5342
    [DIFFICULTY_EASY][TRAINER_MIRROHPEAK_MOXIE] =
    {
#line 5341
        .trainerName = _("Moxie"),
#line 5343
        .trainerClass = TRAINER_CLASS_SOMBER_ADMIN,
#line 5344
        .trainerPic = TRAINER_PIC_SOMBER_ADMIN_MOXIE,
        .encounterMusic_gender =
#line 5346
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 5347
        .items = { ITEM_SUPER_POTION },
#line 5348
        .doubleBattle = FALSE,
#line 5349
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 5350
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 5352
            .species = SPECIES_MORGREM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5352
            .heldItem = ITEM_EVIOLITE,
#line 5355
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 5353
            .ability = ABILITY_PRANKSTER,
#line 5354
            .lvl = 38,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 5356
                MOVE_FAKE_OUT,
                MOVE_DAZZLING_GLEAM,
                MOVE_REFLECT,
                MOVE_LIGHT_SCREEN,
            },
            },
            {
#line 5361
            .species = SPECIES_HONCHKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5361
            .heldItem = ITEM_RAZOR_CLAW,
#line 5364
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 5362
            .ability = ABILITY_SUPER_LUCK,
#line 5363
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 5365
                MOVE_TAUNT,
                MOVE_SUCKER_PUNCH,
                MOVE_AERIAL_ACE,
                MOVE_NIGHT_SLASH,
            },
            },
            {
#line 5370
            .species = SPECIES_SLOWKING_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5370
            .heldItem = ITEM_LEFTOVERS,
#line 5373
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 5371
            .ability = ABILITY_REGENERATOR,
#line 5372
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 5374
                MOVE_TOXIC,
                MOVE_SLUDGE_BOMB,
                MOVE_CALM_MIND,
                MOVE_SLACK_OFF,
            },
            },
            {
#line 5379
            .species = SPECIES_HOUNDOOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5379
            .heldItem = ITEM_HOUNDOOMINITE,
#line 5381
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 5380
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 5382
                MOVE_FLAMETHROWER,
                MOVE_DARK_PULSE,
                MOVE_SLUDGE_BOMB,
                MOVE_NASTY_PLOT,
            },
            },
        },
    },
#line 5387
#line 5389
    [DIFFICULTY_NORMAL][TRAINER_MIRROHPEAK_MOXIE] =
    {
#line 5388
        .trainerName = _("Moxie"),
#line 5390
        .trainerClass = TRAINER_CLASS_SOMBER_ADMIN,
#line 5391
        .trainerPic = TRAINER_PIC_SOMBER_ADMIN_MOXIE,
        .encounterMusic_gender =
#line 5393
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 5394
        .items = { ITEM_FULL_RESTORE },
#line 5395
        .doubleBattle = FALSE,
#line 5396
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_FORCE_SETUP_FIRST_TURN | AI_FLAG_ACE_POKEMON,
#line 5397
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 5399
            .species = SPECIES_MORGREM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5399
            .heldItem = ITEM_EVIOLITE,
#line 5402
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5400
            .ability = ABILITY_PRANKSTER,
#line 5401
            .lvl = 38,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 5402
                MOVE_FAKE_OUT,
                MOVE_DAZZLING_GLEAM,
                MOVE_REFLECT,
                MOVE_LIGHT_SCREEN,
            },
            },
            {
#line 5407
            .species = SPECIES_HONCHKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5407
            .heldItem = ITEM_RAZOR_CLAW,
#line 5410
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5408
            .ability = ABILITY_SUPER_LUCK,
#line 5409
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 5410
                MOVE_TAUNT,
                MOVE_SUCKER_PUNCH,
                MOVE_AERIAL_ACE,
                MOVE_NIGHT_SLASH,
            },
            },
            {
#line 5415
            .species = SPECIES_SLOWKING_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5415
            .heldItem = ITEM_LEFTOVERS,
#line 5418
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5416
            .ability = ABILITY_REGENERATOR,
#line 5417
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 5418
                MOVE_TOXIC,
                MOVE_SLUDGE_BOMB,
                MOVE_CALM_MIND,
                MOVE_SLACK_OFF,
            },
            },
            {
#line 5423
            .species = SPECIES_HOUNDOOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5423
            .heldItem = ITEM_HOUNDOOMINITE,
#line 5425
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5424
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 5425
                MOVE_FLAMETHROWER,
                MOVE_DARK_PULSE,
                MOVE_SLUDGE_BOMB,
                MOVE_NASTY_PLOT,
            },
            },
        },
    },
#line 5444
#line 5446
    [DIFFICULTY_EASY][TRAINER_WINTERLILY_HOLLOW_GYM_A] =
    {
#line 5445
        .trainerName = _("Smirnof"),
#line 5447
        .trainerClass = TRAINER_CLASS_ELECTRICIAN,
#line 5448
        .trainerPic = TRAINER_PIC_ELECTRICIAN,
        .encounterMusic_gender =
#line 5450
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5451
        .doubleBattle = FALSE,
#line 5452
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
#line 5453
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 5455
            .species = SPECIES_TOXTRICITY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5457
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5456
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5459
            .species = SPECIES_GRAVELER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5461
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5460
            .lvl = 35,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5463
#line 5465
    [DIFFICULTY_NORMAL][TRAINER_WINTERLILY_HOLLOW_GYM_A] =
    {
#line 5464
        .trainerName = _("Smirnof"),
#line 5466
        .trainerClass = TRAINER_CLASS_ELECTRICIAN,
#line 5467
        .trainerPic = TRAINER_PIC_ELECTRICIAN,
        .encounterMusic_gender =
#line 5469
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5470
        .doubleBattle = FALSE,
#line 5471
        .aiFlags = AI_FLAG_SMART_TRAINER,
#line 5472
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 5474
            .species = SPECIES_TOXTRICITY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5476
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5475
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5477
            .species = SPECIES_GRAVELER_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5479
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5478
            .lvl = 35,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5495
#line 5497
    [DIFFICULTY_EASY][TRAINER_WINTERLILY_HOLLOW_GYM_B] =
    {
#line 5496
        .trainerName = _("Windhorst"),
#line 5498
        .trainerClass = TRAINER_CLASS_ELECTRICIAN,
#line 5499
        .trainerPic = TRAINER_PIC_ELECTRICIAN,
        .encounterMusic_gender =
#line 5501
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5502
        .doubleBattle = FALSE,
#line 5503
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
#line 5504
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 5506
            .species = SPECIES_KILOWATTREL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5508
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5507
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5510
            .species = SPECIES_BOLTUND,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5512
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5511
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5514
            .species = SPECIES_MAGNETON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5516
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5515
            .lvl = 35,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5518
#line 5520
    [DIFFICULTY_NORMAL][TRAINER_WINTERLILY_HOLLOW_GYM_B] =
    {
#line 5519
        .trainerName = _("Windhorst"),
#line 5521
        .trainerClass = TRAINER_CLASS_ELECTRICIAN,
#line 5522
        .trainerPic = TRAINER_PIC_ELECTRICIAN,
        .encounterMusic_gender =
#line 5524
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5525
        .doubleBattle = FALSE,
#line 5526
        .aiFlags = AI_FLAG_SMART_TRAINER,
#line 5527
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 5529
            .species = SPECIES_KILOWATTREL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5531
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5530
            .lvl = 33,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5532
            .species = SPECIES_BOLTUND,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5534
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5533
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5535
            .species = SPECIES_MAGNETON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5537
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5536
            .lvl = 35,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5550
#line 5552
    [DIFFICULTY_EASY][TRAINER_WINTERLILY_HOLLOW_GYM_C] =
    {
#line 5551
        .trainerName = _("Gozliak"),
#line 5553
        .trainerClass = TRAINER_CLASS_COLLECTOR,
#line 5554
        .trainerPic = TRAINER_PIC_COLLECTOR,
        .encounterMusic_gender =
#line 5556
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5557
        .doubleBattle = FALSE,
#line 5558
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
#line 5559
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5561
            .species = SPECIES_SNEASLER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5561
            .heldItem = ITEM_ELECTRIC_SEED,
#line 5565
            .iv = TRAINER_PARTY_IVS(15, 20, 15, 20, 15, 15),
#line 5562
            .ability = ABILITY_POISON_TOUCH,
#line 5563
            .lvl = 35,
            .nature = NATURE_HARDY,
#line 5564
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 5566
                MOVE_DIRE_CLAW,
                MOVE_CLOSE_COMBAT,
                MOVE_SWORDS_DANCE,
                MOVE_TOXIC,
            },
            },
        },
    },
#line 5571
#line 5573
    [DIFFICULTY_NORMAL][TRAINER_WINTERLILY_HOLLOW_GYM_C] =
    {
#line 5572
        .trainerName = _("Gozliak"),
#line 5574
        .trainerClass = TRAINER_CLASS_COLLECTOR,
#line 5575
        .trainerPic = TRAINER_PIC_COLLECTOR,
        .encounterMusic_gender =
#line 5577
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5578
        .doubleBattle = FALSE,
#line 5579
        .aiFlags = AI_FLAG_SMART_TRAINER,
#line 5580
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5582
            .species = SPECIES_SNEASLER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5582
            .heldItem = ITEM_ELECTRIC_SEED,
#line 5586
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5583
            .ability = ABILITY_POISON_TOUCH,
#line 5584
            .lvl = 35,
            .nature = NATURE_HARDY,
#line 5585
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 5586
                MOVE_DIRE_CLAW,
                MOVE_CLOSE_COMBAT,
                MOVE_SWORDS_DANCE,
                MOVE_TOXIC,
            },
            },
        },
    },
#line 5603
#line 5605
    [DIFFICULTY_EASY][TRAINER_WINTERLILY_HOLLOW_GYM_D] =
    {
#line 5604
        .trainerName = _("Marcus"),
#line 5606
        .trainerClass = TRAINER_CLASS_EMPLOYEE,
#line 5607
        .trainerPic = TRAINER_PIC_EMPLOYEE,
        .encounterMusic_gender =
#line 5609
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5610
        .doubleBattle = FALSE,
#line 5611
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
#line 5612
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 5614
            .species = SPECIES_FURRET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5616
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 5615
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5618
            .species = SPECIES_VOLTORB_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5620
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 5619
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5622
#line 5624
    [DIFFICULTY_NORMAL][TRAINER_WINTERLILY_HOLLOW_GYM_D] =
    {
#line 5623
        .trainerName = _("Marcus"),
#line 5625
        .trainerClass = TRAINER_CLASS_EMPLOYEE,
#line 5626
        .trainerPic = TRAINER_PIC_EMPLOYEE,
        .encounterMusic_gender =
#line 5628
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5629
        .doubleBattle = FALSE,
#line 5630
        .aiFlags = AI_FLAG_SMART_TRAINER,
#line 5631
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 5633
            .species = SPECIES_FURRET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5635
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5634
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5636
            .species = SPECIES_VOLTORB_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5638
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5637
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5648
#line 5650
    [DIFFICULTY_EASY][TRAINER_WINTERLILY_HOLLOW_GYM_E] =
    {
#line 5649
        .trainerName = _("Bleach"),
#line 5651
        .trainerClass = TRAINER_CLASS_EMPLOYEE,
#line 5652
        .trainerPic = TRAINER_PIC_EMPLOYEE,
        .encounterMusic_gender =
#line 5654
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5655
        .doubleBattle = FALSE,
#line 5656
        .aiFlags = AI_FLAG_BASIC_TRAINER,
#line 5657
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 5659
            .species = SPECIES_CHINCHOU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5661
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 5660
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5663
            .species = SPECIES_BOLTUND,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5665
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 5664
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5668
#line 5670
    [DIFFICULTY_NORMAL][TRAINER_WINTERLILY_HOLLOW_GYM_E] =
    {
#line 5669
        .trainerName = _("Bleach"),
#line 5671
        .trainerClass = TRAINER_CLASS_EMPLOYEE,
#line 5672
        .trainerPic = TRAINER_PIC_EMPLOYEE,
        .encounterMusic_gender =
#line 5674
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5675
        .doubleBattle = FALSE,
#line 5676
        .aiFlags = AI_FLAG_SMART_TRAINER,
#line 5677
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 5679
            .species = SPECIES_CHINCHOU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5681
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5680
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5682
            .species = SPECIES_BOLTUND,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5684
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5683
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5697
#line 5699
    [DIFFICULTY_EASY][TRAINER_WINTERLILY_HOLLOW_GYM_F] =
    {
#line 5698
        .trainerName = _("Tamaron"),
#line 5700
        .trainerClass = TRAINER_CLASS_ELECTRICIAN,
#line 5701
        .trainerPic = TRAINER_PIC_ELECTRICIAN,
        .encounterMusic_gender =
#line 5703
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5704
        .doubleBattle = FALSE,
#line 5705
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
#line 5706
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5708
            .species = SPECIES_KILOWATTREL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5708
            .heldItem = ITEM_ELECTRIC_SEED,
#line 5710
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5709
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5712
#line 5714
    [DIFFICULTY_NORMAL][TRAINER_WINTERLILY_HOLLOW_GYM_F] =
    {
#line 5713
        .trainerName = _("Tamaron"),
#line 5715
        .trainerClass = TRAINER_CLASS_ELECTRICIAN,
#line 5716
        .trainerPic = TRAINER_PIC_ELECTRICIAN,
        .encounterMusic_gender =
#line 5718
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5719
        .doubleBattle = FALSE,
#line 5720
        .aiFlags = AI_FLAG_SMART_TRAINER,
#line 5721
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 5723
            .species = SPECIES_KILOWATTREL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5723
            .heldItem = ITEM_ELECTRIC_SEED,
#line 5725
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5724
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5737
#line 5739
    [DIFFICULTY_EASY][TRAINER_WINTERLILY_HOLLOW_GYM_LEADER] =
    {
#line 5738
        .trainerName = _("Viniel"),
#line 5740
        .trainerClass = TRAINER_CLASS_LEADER,
#line 5741
        .trainerPic = TRAINER_PIC_LEADER_VINIEL,
        .encounterMusic_gender =
#line 5743
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5744
        .doubleBattle = FALSE,
#line 5745
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 5747
        .mugshotColor = MUGSHOT_COLOR_YELLOW,
#line 5746
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 5749
            .species = SPECIES_KILOWATTREL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5749
            .heldItem = ITEM_FOCUS_SASH,
#line 5751
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5750
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5753
            .species = SPECIES_TOXTRICITY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5753
            .heldItem = ITEM_THROAT_SPRAY,
#line 5755
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5754
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5757
            .species = SPECIES_LANTURN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5757
            .heldItem = ITEM_ELECTRIC_SEED,
#line 5759
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5758
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5761
            .species = SPECIES_MANECTRIC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5761
            .heldItem = ITEM_MANECTITE,
#line 5763
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5762
            .lvl = 43,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5765
#line 5767
    [DIFFICULTY_NORMAL][TRAINER_WINTERLILY_HOLLOW_GYM_LEADER] =
    {
#line 5766
        .trainerName = _("Viniel"),
#line 5768
        .trainerClass = TRAINER_CLASS_LEADER,
#line 5769
        .trainerPic = TRAINER_PIC_LEADER_VINIEL,
        .encounterMusic_gender =
#line 5771
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5772
        .doubleBattle = FALSE,
#line 5773
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 5775
        .mugshotColor = MUGSHOT_COLOR_YELLOW,
#line 5774
        .startingStatus = STARTING_STATUS_ELECTRIC_TERRAIN,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 5777
            .species = SPECIES_KILOWATTREL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5777
            .heldItem = ITEM_FOCUS_SASH,
#line 5779
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5778
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5780
            .species = SPECIES_TOXTRICITY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5780
            .heldItem = ITEM_THROAT_SPRAY,
#line 5782
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5781
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5783
            .species = SPECIES_LANTURN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5783
            .heldItem = ITEM_ELECTRIC_SEED,
#line 5785
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5784
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5786
            .species = SPECIES_MANECTRIC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5786
            .heldItem = ITEM_MANECTITE,
#line 5788
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5787
            .lvl = 45,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5806
#line 5808
    [DIFFICULTY_EASY][TRAINER_PELLUCA_CITY_GYM_A] =
    {
#line 5807
        .trainerName = _("Gabrielle"),
#line 5809
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 5810
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 5811
F_TRAINER_FEMALE | 
#line 5812
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 5813
        .doubleBattle = FALSE,
#line 5814
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 5816
            .species = SPECIES_ZOROARK_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5818
            .iv = TRAINER_PARTY_IVS(18, 18, 18, 18, 18, 18),
#line 5817
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5820
            .species = SPECIES_CLAYDOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5822
            .iv = TRAINER_PARTY_IVS(18, 18, 18, 18, 18, 18),
#line 5821
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5824
            .species = SPECIES_HAKAMO_O,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5826
            .iv = TRAINER_PARTY_IVS(18, 18, 18, 18, 18, 18),
#line 5825
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5828
            .species = SPECIES_MAWILE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5830
            .iv = TRAINER_PARTY_IVS(18, 18, 18, 18, 18, 18),
#line 5829
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5832
#line 5834
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_CITY_GYM_A] =
    {
#line 5833
        .trainerName = _("Gabrielle"),
#line 5835
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 5836
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 5837
F_TRAINER_FEMALE | 
#line 5838
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 5839
        .doubleBattle = FALSE,
#line 5840
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 5842
            .species = SPECIES_ZOROARK_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5844
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5843
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5845
            .species = SPECIES_CLAYDOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5847
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5846
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5848
            .species = SPECIES_HAKAMO_O,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5850
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5849
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5851
            .species = SPECIES_MAWILE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5853
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5852
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5869
#line 5871
    [DIFFICULTY_EASY][TRAINER_PELLUCA_CITY_GYM_B] =
    {
#line 5870
        .trainerName = _("JL"),
#line 5872
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 5873
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 5875
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5876
        .doubleBattle = FALSE,
#line 5877
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 5879
            .species = SPECIES_LAMPENT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5881
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5880
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5883
            .species = SPECIES_DELPHOX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5883
            .heldItem = ITEM_LEFTOVERS,
#line 5885
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5884
            .lvl = 40,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5887
            .species = SPECIES_DREEPY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5889
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5888
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5891
#line 5893
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_CITY_GYM_B] =
    {
#line 5892
        .trainerName = _("JL"),
#line 5894
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 5895
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 5897
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 5898
        .doubleBattle = FALSE,
#line 5899
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 5901
            .species = SPECIES_LAMPENT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5903
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5902
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5904
            .species = SPECIES_DELPHOX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5904
            .heldItem = ITEM_LEFTOVERS,
#line 5906
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5905
            .lvl = 40,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5907
            .species = SPECIES_DREEPY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5909
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5908
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5919
#line 5921
    [DIFFICULTY_EASY][TRAINER_PELLUCA_CITY_GYM_C] =
    {
#line 5920
        .trainerName = _("Laria"),
#line 5922
        .trainerClass = TRAINER_CLASS_SWIMMER_F,
#line 5923
        .trainerPic = TRAINER_PIC_SWIMMER_F,
        .encounterMusic_gender =
#line 5924
F_TRAINER_FEMALE | 
#line 5925
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 5926
        .doubleBattle = FALSE,
#line 5927
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 5929
            .species = SPECIES_CURSOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5931
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5930
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5933
            .species = SPECIES_BARRASKEWDA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5935
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5934
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5937
#line 5939
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_CITY_GYM_C] =
    {
#line 5938
        .trainerName = _("Laria"),
#line 5940
        .trainerClass = TRAINER_CLASS_SWIMMER_F,
#line 5941
        .trainerPic = TRAINER_PIC_SWIMMER_F,
        .encounterMusic_gender =
#line 5942
F_TRAINER_FEMALE | 
#line 5943
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 5944
        .doubleBattle = FALSE,
#line 5945
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 5947
            .species = SPECIES_CURSOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5949
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5948
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5950
            .species = SPECIES_BARRASKEWDA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5952
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5951
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5964
#line 5966
    [DIFFICULTY_EASY][TRAINER_PELLUCA_CITY_GYM_D] =
    {
#line 5965
        .trainerName = _("Mollen"),
#line 5967
        .trainerClass = TRAINER_CLASS_SWIMMER_M,
#line 5968
        .trainerPic = TRAINER_PIC_SWIMMER_M,
        .encounterMusic_gender =
#line 5970
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 5971
        .doubleBattle = FALSE,
#line 5972
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 5974
            .species = SPECIES_MASQUERAIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5976
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5975
            .lvl = 40,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5978
            .species = SPECIES_CARVANHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5980
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 5979
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 5983
#line 5985
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_CITY_GYM_D] =
    {
#line 5984
        .trainerName = _("Mollen"),
#line 5986
        .trainerClass = TRAINER_CLASS_SWIMMER_M,
#line 5987
        .trainerPic = TRAINER_PIC_SWIMMER_M,
        .encounterMusic_gender =
#line 5989
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 5990
        .doubleBattle = FALSE,
#line 5991
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 5993
            .species = SPECIES_MASQUERAIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5995
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5994
            .lvl = 40,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 5996
            .species = SPECIES_CARVANHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 5998
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 5997
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6010
#line 6012
    [DIFFICULTY_EASY][TRAINER_PELLUCA_CITY_GYM_E] =
    {
#line 6011
        .trainerName = _("Jasmina"),
#line 6013
        .trainerClass = TRAINER_CLASS_BEAUTY,
#line 6014
        .trainerPic = TRAINER_PIC_BEAUTY,
        .encounterMusic_gender =
#line 6015
F_TRAINER_FEMALE | 
#line 6016
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 6017
        .items = { ITEM_FULL_RESTORE },
#line 6018
        .doubleBattle = FALSE,
#line 6019
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6021
            .species = SPECIES_DEWPIDER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6023
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 6022
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6025
            .species = SPECIES_PALPITOAD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6027
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 6026
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6029
#line 6031
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_CITY_GYM_E] =
    {
#line 6030
        .trainerName = _("Jasmina"),
#line 6032
        .trainerClass = TRAINER_CLASS_BEAUTY,
#line 6033
        .trainerPic = TRAINER_PIC_BEAUTY,
        .encounterMusic_gender =
#line 6034
F_TRAINER_FEMALE | 
#line 6035
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 6036
        .items = { ITEM_FULL_RESTORE },
#line 6037
        .doubleBattle = FALSE,
#line 6038
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6040
            .species = SPECIES_DEWPIDER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6042
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6041
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6043
            .species = SPECIES_PALPITOAD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6045
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6044
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6059
#line 6061
    [DIFFICULTY_EASY][TRAINER_PELLUCA_CITY_GYM_F] =
    {
#line 6060
        .trainerName = _("Arya"),
#line 6062
        .trainerClass = TRAINER_CLASS_SWIMMER_F,
#line 6063
        .trainerPic = TRAINER_PIC_SWIMMER_F,
        .encounterMusic_gender =
#line 6065
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 6066
        .doubleBattle = FALSE,
#line 6067
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6069
            .species = SPECIES_SKRELP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6071
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 6070
            .lvl = 40,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6073
#line 6075
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_CITY_GYM_F] =
    {
#line 6074
        .trainerName = _("Arya"),
#line 6076
        .trainerClass = TRAINER_CLASS_SWIMMER_F,
#line 6077
        .trainerPic = TRAINER_PIC_SWIMMER_F,
        .encounterMusic_gender =
#line 6079
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 6080
        .doubleBattle = FALSE,
#line 6081
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6083
            .species = SPECIES_SKRELP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6085
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6084
            .lvl = 40,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6100
#line 6102
    [DIFFICULTY_EASY][TRAINER_PELLUCA_CITY_GYM_G] =
    {
#line 6101
        .trainerName = _("Wint"),
#line 6103
        .trainerClass = TRAINER_CLASS_SWIMMER_M,
#line 6104
        .trainerPic = TRAINER_PIC_SWIMMER_M,
        .encounterMusic_gender =
#line 6106
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 6107
        .doubleBattle = FALSE,
#line 6108
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6110
            .species = SPECIES_BRUXISH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6112
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 6111
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6114
#line 6116
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_CITY_GYM_G] =
    {
#line 6115
        .trainerName = _("Wint"),
#line 6117
        .trainerClass = TRAINER_CLASS_SWIMMER_M,
#line 6118
        .trainerPic = TRAINER_PIC_SWIMMER_M,
        .encounterMusic_gender =
#line 6120
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 6121
        .doubleBattle = FALSE,
#line 6122
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6124
            .species = SPECIES_BRUXISH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6126
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6125
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6141
#line 6143
    [DIFFICULTY_EASY][TRAINER_PELLUCA_CITY_GYM_H] =
    {
#line 6142
        .trainerName = _("Winston"),
#line 6144
        .trainerClass = TRAINER_CLASS_RICH_BOY,
#line 6145
        .trainerPic = TRAINER_PIC_RICH_BOY,
        .encounterMusic_gender =
#line 6147
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 6148
        .items = { ITEM_FULL_RESTORE },
#line 6149
        .doubleBattle = FALSE,
#line 6150
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 6152
            .species = SPECIES_MAREANIE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6154
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 6153
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6156
            .species = SPECIES_QWILFISH_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6158
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 6157
            .lvl = 40,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6160
            .species = SPECIES_MASQUERAIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6162
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 6161
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6164
#line 6166
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_CITY_GYM_H] =
    {
#line 6165
        .trainerName = _("Winston"),
#line 6167
        .trainerClass = TRAINER_CLASS_RICH_BOY,
#line 6168
        .trainerPic = TRAINER_PIC_RICH_BOY,
        .encounterMusic_gender =
#line 6170
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 6171
        .items = { ITEM_FULL_RESTORE },
#line 6172
        .doubleBattle = FALSE,
#line 6173
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 6175
            .species = SPECIES_MAREANIE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6177
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6176
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6178
            .species = SPECIES_QWILFISH_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6180
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6179
            .lvl = 40,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6181
            .species = SPECIES_MASQUERAIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6183
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6182
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6194
#line 6196
    [DIFFICULTY_EASY][TRAINER_PELLUCA_CITY_GYM_I] =
    {
#line 6195
        .trainerName = _("Winston"),
#line 6197
        .trainerClass = TRAINER_CLASS_RICH_BOY,
#line 6198
        .trainerPic = TRAINER_PIC_RICH_BOY,
        .encounterMusic_gender =
#line 6200
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 6201
        .items = { ITEM_FULL_RESTORE },
#line 6202
        .doubleBattle = FALSE,
#line 6203
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6205
            .species = SPECIES_LAPRAS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6207
            .iv = TRAINER_PARTY_IVS(15, 15, 15, 15, 15, 15),
#line 6206
            .lvl = 43,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6209
#line 6211
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_CITY_GYM_I] =
    {
#line 6210
        .trainerName = _("Winston"),
#line 6212
        .trainerClass = TRAINER_CLASS_RICH_BOY,
#line 6213
        .trainerPic = TRAINER_PIC_RICH_BOY,
        .encounterMusic_gender =
#line 6215
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 6216
        .items = { ITEM_FULL_RESTORE },
#line 6217
        .doubleBattle = FALSE,
#line 6218
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6220
            .species = SPECIES_LAPRAS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6222
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6221
            .lvl = 43,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6241
#line 6243
    [DIFFICULTY_EASY][TRAINER_PELLUCA_CITY_GYM_LEADER] =
    {
#line 6242
        .trainerName = _("Jania"),
#line 6244
        .trainerClass = TRAINER_CLASS_LEADER,
#line 6245
        .trainerPic = TRAINER_PIC_LEADER_JANIA,
        .encounterMusic_gender =
#line 6246
F_TRAINER_FEMALE | 
#line 6247
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 6248
        .doubleBattle = FALSE,
#line 6249
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 6250
        .mugshotColor = MUGSHOT_COLOR_BLUE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 6252
            .species = SPECIES_PELIPPER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6252
            .heldItem = ITEM_DAMP_ROCK,
#line 6255
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 6253
            .ability = ABILITY_DRIZZLE,
#line 6254
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 6256
                MOVE_RAIN_DANCE,
                MOVE_HURRICANE,
                MOVE_MUDDY_WATER,
            },
            },
            {
#line 6260
            .species = SPECIES_CLAWITZER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6260
            .heldItem = ITEM_CHOICE_SPECS,
#line 6263
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 6261
            .ability = ABILITY_MEGA_LAUNCHER,
#line 6262
            .lvl = 43,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 6264
                MOVE_WATER_PULSE,
            },
            },
            {
#line 6266
            .species = SPECIES_TOXAPEX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6266
            .heldItem = ITEM_BLACK_SLUDGE,
#line 6268
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 6267
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 6269
                MOVE_MUDDY_WATER,
                MOVE_TOXIC,
                MOVE_BANEFUL_BUNKER,
                MOVE_RECOVER,
            },
            },
            {
#line 6274
            .species = SPECIES_TOEDSCRUEL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6274
            .heldItem = ITEM_LEFTOVERS,
#line 6276
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 6275
            .lvl = 43,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6278
            .species = SPECIES_GYARADOS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6278
            .heldItem = ITEM_GYARADOSITE,
#line 6280
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 6279
            .lvl = 45,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6282
#line 6284
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_CITY_GYM_LEADER] =
    {
#line 6283
        .trainerName = _("Jania"),
#line 6285
        .trainerClass = TRAINER_CLASS_LEADER,
#line 6286
        .trainerPic = TRAINER_PIC_LEADER_JANIA,
        .encounterMusic_gender =
#line 6287
F_TRAINER_FEMALE | 
#line 6288
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 6289
        .doubleBattle = FALSE,
#line 6290
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_RISKY | AI_FLAG_ACE_POKEMON,
#line 6291
        .mugshotColor = MUGSHOT_COLOR_BLUE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 6293
            .species = SPECIES_PELIPPER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6293
            .heldItem = ITEM_DAMP_ROCK,
#line 6296
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6294
            .ability = ABILITY_DRIZZLE,
#line 6295
            .lvl = 41,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 6296
                MOVE_RAIN_DANCE,
                MOVE_HURRICANE,
                MOVE_MUDDY_WATER,
            },
            },
            {
#line 6300
            .species = SPECIES_CLAWITZER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6300
            .heldItem = ITEM_CHOICE_SPECS,
#line 6303
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6301
            .ability = ABILITY_MEGA_LAUNCHER,
#line 6302
            .lvl = 43,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 6303
                MOVE_WATER_PULSE,
            },
            },
            {
#line 6305
            .species = SPECIES_TOXAPEX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6305
            .heldItem = ITEM_BLACK_SLUDGE,
#line 6307
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6306
            .lvl = 42,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 6307
                MOVE_MUDDY_WATER,
                MOVE_TOXIC,
                MOVE_BANEFUL_BUNKER,
                MOVE_RECOVER,
            },
            },
            {
#line 6312
            .species = SPECIES_TOEDSCRUEL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6312
            .heldItem = ITEM_LEFTOVERS,
#line 6314
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6313
            .lvl = 43,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6315
            .species = SPECIES_GYARADOS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6315
            .heldItem = ITEM_GYARADOSITE,
#line 6317
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6316
            .lvl = 45,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6335
#line 6337
    [DIFFICULTY_EASY][TRAINER_ROUTE3_EXT_A] =
    {
#line 6336
        .trainerName = _("Flanning"),
#line 6338
        .trainerClass = TRAINER_CLASS_BIRD_KEEPER,
#line 6339
        .trainerPic = TRAINER_PIC_BIRD_KEEPER,
        .encounterMusic_gender =
#line 6341
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 6342
        .doubleBattle = FALSE,
#line 6343
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6345
            .species = SPECIES_NOIBAT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6347
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 6346
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6349
            .species = SPECIES_FLETCHINDER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6351
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 6350
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6353
#line 6355
    [DIFFICULTY_NORMAL][TRAINER_ROUTE3_EXT_A] =
    {
#line 6354
        .trainerName = _("Flanning"),
#line 6356
        .trainerClass = TRAINER_CLASS_BIRD_KEEPER,
#line 6357
        .trainerPic = TRAINER_PIC_BIRD_KEEPER,
        .encounterMusic_gender =
#line 6359
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 6360
        .doubleBattle = FALSE,
#line 6361
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6363
            .species = SPECIES_NOIBAT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6365
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6364
            .lvl = 22,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6366
            .species = SPECIES_FLETCHINDER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6368
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6367
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6381
#line 6383
    [DIFFICULTY_EASY][TRAINER_ROUTE3_EXT_B] =
    {
#line 6382
        .trainerName = _("Barkle"),
#line 6384
        .trainerClass = TRAINER_CLASS_BLACK_BELT,
#line 6385
        .trainerPic = TRAINER_PIC_BLACK_BELT,
        .encounterMusic_gender =
#line 6387
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 6388
        .doubleBattle = FALSE,
#line 6389
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6391
            .species = SPECIES_MANKEY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6393
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 6392
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6395
            .species = SPECIES_SNEASEL_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6397
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 6396
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6399
#line 6401
    [DIFFICULTY_NORMAL][TRAINER_ROUTE3_EXT_B] =
    {
#line 6400
        .trainerName = _("Barkle"),
#line 6402
        .trainerClass = TRAINER_CLASS_BLACK_BELT,
#line 6403
        .trainerPic = TRAINER_PIC_BLACK_BELT,
        .encounterMusic_gender =
#line 6405
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 6406
        .doubleBattle = FALSE,
#line 6407
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6409
            .species = SPECIES_MANKEY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6411
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6410
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6412
            .species = SPECIES_SNEASEL_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6414
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6413
            .lvl = 23,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6426
#line 6428
    [DIFFICULTY_EASY][TRAINER_ROUTE3_EXT_C] =
    {
#line 6427
        .trainerName = _("Grim"),
#line 6429
        .trainerClass = TRAINER_CLASS_BACKPACKER,
#line 6430
        .trainerPic = TRAINER_PIC_BACKPACKER,
        .encounterMusic_gender =
#line 6432
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 6433
        .doubleBattle = FALSE,
#line 6434
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6436
            .species = SPECIES_MIMIKYU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6438
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6437
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6439
#line 6441
    [DIFFICULTY_NORMAL][TRAINER_ROUTE3_EXT_C] =
    {
#line 6440
        .trainerName = _("Grim"),
#line 6442
        .trainerClass = TRAINER_CLASS_BACKPACKER,
#line 6443
        .trainerPic = TRAINER_PIC_BACKPACKER,
        .encounterMusic_gender =
#line 6445
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 6446
        .doubleBattle = FALSE,
#line 6447
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6449
            .species = SPECIES_MIMIKYU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6451
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6450
            .lvl = 21,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6467
#line 6469
    [DIFFICULTY_EASY][TRAINER_PELLUCA_QWILSQUAD_A] =
    {
#line 6468
        .trainerName = _("Grunt"),
#line 6470
        .trainerClass = TRAINER_CLASS_SAILOR,
#line 6471
        .trainerPic = TRAINER_PIC_SAILOR,
        .encounterMusic_gender =
#line 6473
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 6474
        .doubleBattle = FALSE,
#line 6475
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6477
            .species = SPECIES_DHELMISE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6479
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 6478
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6481
            .species = SPECIES_QWILFISH_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6483
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 6482
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6485
#line 6487
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_QWILSQUAD_A] =
    {
#line 6486
        .trainerName = _("Grunt"),
#line 6488
        .trainerClass = TRAINER_CLASS_SAILOR,
#line 6489
        .trainerPic = TRAINER_PIC_SAILOR,
        .encounterMusic_gender =
#line 6491
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 6492
        .doubleBattle = FALSE,
#line 6493
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6495
            .species = SPECIES_DHELMISE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6497
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6496
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6498
            .species = SPECIES_QWILFISH_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6500
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6499
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6519
#line 6521
    [DIFFICULTY_EASY][TRAINER_PELLUCA_QWILSQUAD_B] =
    {
#line 6520
        .trainerName = _("Grunt"),
#line 6522
        .trainerClass = TRAINER_CLASS_SAILOR,
#line 6523
        .trainerPic = TRAINER_PIC_SAILOR,
        .encounterMusic_gender =
#line 6525
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 6526
        .doubleBattle = FALSE,
#line 6527
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6529
            .species = SPECIES_CARVANHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6531
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 6530
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6533
            .species = SPECIES_QWILFISH_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6535
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 6534
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6537
#line 6539
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_QWILSQUAD_B] =
    {
#line 6538
        .trainerName = _("Grunt"),
#line 6540
        .trainerClass = TRAINER_CLASS_SAILOR,
#line 6541
        .trainerPic = TRAINER_PIC_SAILOR,
        .encounterMusic_gender =
#line 6543
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 6544
        .doubleBattle = FALSE,
#line 6545
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6547
            .species = SPECIES_CARVANHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6549
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6548
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6550
            .species = SPECIES_QWILFISH_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6552
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6551
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6563
#line 6565
    [DIFFICULTY_EASY][TRAINER_PELLUCA_QWILSQUAD_BOSS] =
    {
#line 6564
        .trainerName = _("Boss"),
#line 6566
        .trainerClass = TRAINER_CLASS_SAILOR,
#line 6567
        .trainerPic = TRAINER_PIC_QWILSQUAD_BOSS,
        .encounterMusic_gender =
#line 6569
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 6570
        .doubleBattle = FALSE,
#line 6571
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 6572
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 6574
            .species = SPECIES_LAIRON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6576
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 6575
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6578
            .species = SPECIES_DHELMISE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6580
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 6579
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6582
            .species = SPECIES_OVERQWIL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6584
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 6583
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6586
#line 6588
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_QWILSQUAD_BOSS] =
    {
#line 6587
        .trainerName = _("Boss"),
#line 6589
        .trainerClass = TRAINER_CLASS_SAILOR,
#line 6590
        .trainerPic = TRAINER_PIC_QWILSQUAD_BOSS,
        .encounterMusic_gender =
#line 6592
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 6593
        .items = { ITEM_SUPER_POTION },
#line 6594
        .doubleBattle = FALSE,
#line 6595
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 6596
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 6598
            .species = SPECIES_LAIRON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6600
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6599
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6601
            .species = SPECIES_DHELMISE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6603
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6602
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6604
            .species = SPECIES_OVERQWIL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6606
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6605
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6620
#line 6622
    [DIFFICULTY_EASY][TRAINER_PELLUCA_GAMBLER] =
    {
#line 6621
        .trainerName = _("Chaina"),
#line 6623
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 6624
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 6625
F_TRAINER_FEMALE | 
#line 6626
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 6627
        .doubleBattle = FALSE,
#line 6628
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 6631
            .species = SPECIES_FEEBAS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6633
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 6632
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 6634
                MOVE_SCALE_SHOT,
            },
            },
            {
#line 6636
            .species = SPECIES_BAYLEEF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6638
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 6637
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 6639
                MOVE_BULLET_SEED,
            },
            },
            {
#line 6641
            .species = SPECIES_DUGTRIO_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6643
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 6642
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 6644
                MOVE_ROCK_BLAST,
            },
            },
        },
    },
#line 6646
#line 6648
    [DIFFICULTY_NORMAL][TRAINER_PELLUCA_GAMBLER] =
    {
#line 6647
        .trainerName = _("Chaina"),
#line 6649
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 6650
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 6651
F_TRAINER_FEMALE | 
#line 6652
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 6653
        .doubleBattle = FALSE,
#line 6654
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 6657
            .species = SPECIES_FEEBAS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6657
            .heldItem = ITEM_LOADED_DICE,
#line 6659
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6658
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 6659
                MOVE_SCALE_SHOT,
            },
            },
            {
#line 6661
            .species = SPECIES_BAYLEEF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6661
            .heldItem = ITEM_LOADED_DICE,
#line 6663
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6662
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 6663
                MOVE_BULLET_SEED,
            },
            },
            {
#line 6665
            .species = SPECIES_DUGTRIO_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6665
            .heldItem = ITEM_LOADED_DICE,
#line 6667
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6666
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 6667
                MOVE_ROCK_BLAST,
            },
            },
        },
    },
#line 6679
#line 6681
    [DIFFICULTY_EASY][TRAINER_ROUTE8_A] =
    {
#line 6680
        .trainerName = _("Lana"),
#line 6682
        .trainerClass = TRAINER_CLASS_SWIMMER_F,
#line 6683
        .trainerPic = TRAINER_PIC_SWIMMER_F,
        .encounterMusic_gender =
#line 6685
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 6686
        .doubleBattle = FALSE,
#line 6687
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6689
            .species = SPECIES_CARVANHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6691
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 6690
            .lvl = 45,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6693
#line 6695
    [DIFFICULTY_NORMAL][TRAINER_ROUTE8_A] =
    {
#line 6694
        .trainerName = _("Lana"),
#line 6696
        .trainerClass = TRAINER_CLASS_SWIMMER_F,
#line 6697
        .trainerPic = TRAINER_PIC_SWIMMER_F,
        .encounterMusic_gender =
#line 6699
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 6700
        .doubleBattle = FALSE,
#line 6701
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6703
            .species = SPECIES_CARVANHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6705
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6704
            .lvl = 45,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6716
#line 6718
    [DIFFICULTY_EASY][TRAINER_ROUTE8_B] =
    {
#line 6717
        .trainerName = _("Danneon"),
#line 6719
        .trainerClass = TRAINER_CLASS_SWIMMER_M,
#line 6720
        .trainerPic = TRAINER_PIC_SWIMMER_M,
        .encounterMusic_gender =
#line 6722
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 6723
        .doubleBattle = FALSE,
#line 6724
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6726
            .species = SPECIES_TOEDSCRUEL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6728
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6727
            .lvl = 44,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6729
#line 6731
    [DIFFICULTY_NORMAL][TRAINER_ROUTE8_B] =
    {
#line 6730
        .trainerName = _("Danneon"),
#line 6732
        .trainerClass = TRAINER_CLASS_SWIMMER_M,
#line 6733
        .trainerPic = TRAINER_PIC_SWIMMER_M,
        .encounterMusic_gender =
#line 6735
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 6736
        .doubleBattle = FALSE,
#line 6737
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6739
            .species = SPECIES_TOEDSCRUEL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6741
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6740
            .lvl = 44,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6753
#line 6755
    [DIFFICULTY_EASY][TRAINER_ROUTE8_C] =
    {
#line 6754
        .trainerName = _("Pralia"),
#line 6756
        .trainerClass = TRAINER_CLASS_AROMA_LADY,
#line 6757
        .trainerPic = TRAINER_PIC_AROMA_LADY,
        .encounterMusic_gender =
#line 6759
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 6760
        .doubleBattle = FALSE,
#line 6761
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6763
            .species = SPECIES_ROSELIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6765
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 6764
            .lvl = 45,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6767
            .species = SPECIES_MEGANIUM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6769
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 6768
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6771
#line 6773
    [DIFFICULTY_NORMAL][TRAINER_ROUTE8_C] =
    {
#line 6772
        .trainerName = _("Pralia"),
#line 6774
        .trainerClass = TRAINER_CLASS_AROMA_LADY,
#line 6775
        .trainerPic = TRAINER_PIC_AROMA_LADY,
        .encounterMusic_gender =
#line 6777
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 6778
        .doubleBattle = FALSE,
#line 6779
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6781
            .species = SPECIES_ROSERADE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6783
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6782
            .lvl = 45,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6784
            .species = SPECIES_MEGANIUM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6786
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6785
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6799
#line 6801
    [DIFFICULTY_EASY][TRAINER_ROUTE8_D] =
    {
#line 6800
        .trainerName = _("Mary"),
#line 6802
        .trainerClass = TRAINER_CLASS_PSYCHIC,
#line 6803
        .trainerPic = TRAINER_PIC_PSYCHIC_F,
        .encounterMusic_gender =
#line 6804
F_TRAINER_FEMALE | 
#line 6805
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 6806
        .doubleBattle = FALSE,
#line 6807
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6809
            .species = SPECIES_KIRLIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6811
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 6810
            .lvl = 44,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6813
            .species = SPECIES_BRAVIARY_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6815
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 6814
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6818
#line 6820
    [DIFFICULTY_NORMAL][TRAINER_ROUTE8_D] =
    {
#line 6819
        .trainerName = _("Mary"),
#line 6821
        .trainerClass = TRAINER_CLASS_PSYCHIC,
#line 6822
        .trainerPic = TRAINER_PIC_PSYCHIC_F,
        .encounterMusic_gender =
#line 6823
F_TRAINER_FEMALE | 
#line 6824
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 6825
        .doubleBattle = FALSE,
#line 6826
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_TRY_TO_FAINT,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6828
            .species = SPECIES_KIRLIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6830
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6829
            .lvl = 44,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6831
            .species = SPECIES_BRAVIARY_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6833
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6832
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6846
#line 6848
    [DIFFICULTY_EASY][TRAINER_ROUTE8_E] =
    {
#line 6847
        .trainerName = _("Bony"),
#line 6849
        .trainerClass = TRAINER_CLASS_SWIMMER_M,
#line 6850
        .trainerPic = TRAINER_PIC_SWIMMER_M,
        .encounterMusic_gender =
#line 6852
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 6853
        .doubleBattle = FALSE,
#line 6854
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6856
            .species = SPECIES_CARVANHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6858
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 6857
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6860
#line 6862
    [DIFFICULTY_EASY][TRAINER_ROUTE8_F] =
    {
#line 6861
        .trainerName = _("Jirra"),
#line 6863
        .trainerClass = TRAINER_CLASS_SWIMMER_M,
#line 6864
        .trainerPic = TRAINER_PIC_SWIMMER_M,
        .encounterMusic_gender =
#line 6866
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 6867
        .doubleBattle = FALSE,
#line 6868
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6870
            .species = SPECIES_TENTACRUEL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6872
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 6871
            .lvl = 26,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6883
#line 6885
    [DIFFICULTY_EASY][TRAINER_RIVETSHORE_GYM_A] =
    {
#line 6884
        .trainerName = _("Matti"),
#line 6886
        .trainerClass = TRAINER_CLASS_BUILDER,
#line 6887
        .trainerPic = TRAINER_PIC_BUILDER,
        .encounterMusic_gender =
#line 6889
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 6890
        .doubleBattle = FALSE,
#line 6891
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6893
            .species = SPECIES_DUGTRIO_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6895
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 6894
            .lvl = 44,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6897
            .species = SPECIES_SKARMORY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6899
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 6898
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6901
#line 6903
    [DIFFICULTY_NORMAL][TRAINER_RIVETSHORE_GYM_A] =
    {
#line 6902
        .trainerName = _("Matti"),
#line 6904
        .trainerClass = TRAINER_CLASS_BUILDER,
#line 6905
        .trainerPic = TRAINER_PIC_BUILDER,
        .encounterMusic_gender =
#line 6907
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 6908
        .doubleBattle = FALSE,
#line 6909
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 6911
            .species = SPECIES_DUGTRIO_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6913
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6912
            .lvl = 44,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6914
            .species = SPECIES_SKARMORY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6914
            .heldItem = ITEM_SITRUS_BERRY,
#line 6916
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6915
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6929
#line 6931
    [DIFFICULTY_EASY][TRAINER_RIVETSHORE_GYM_B] =
    {
#line 6930
        .trainerName = _("Berger"),
#line 6932
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 6933
        .trainerPic = TRAINER_PIC_COOL_GUY,
        .encounterMusic_gender =
#line 6935
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 6936
        .doubleBattle = FALSE,
#line 6937
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 6939
            .species = SPECIES_TINKATUFF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6941
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 6940
            .lvl = 43,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6943
            .species = SPECIES_ARCTIBAX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6945
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 6944
            .lvl = 44,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6947
            .species = SPECIES_AVALUGG_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6949
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 6948
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6951
#line 6953
    [DIFFICULTY_NORMAL][TRAINER_RIVETSHORE_GYM_B] =
    {
#line 6952
        .trainerName = _("Berger"),
#line 6954
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 6955
        .trainerPic = TRAINER_PIC_COOL_GUY,
        .encounterMusic_gender =
#line 6957
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 6959
        .items = { ITEM_FULL_RESTORE },
#line 6958
        .doubleBattle = FALSE,
#line 6960
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 6962
            .species = SPECIES_TINKATUFF,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6962
            .heldItem = ITEM_LEFTOVERS,
#line 6964
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6963
            .lvl = 43,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6965
            .species = SPECIES_ARCTIBAX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6965
            .heldItem = ITEM_DRAGON_GEM,
#line 6967
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6966
            .lvl = 44,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 6968
            .species = SPECIES_AVALUGG_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6968
            .heldItem = ITEM_SALAC_BERRY,
#line 6970
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 6969
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 6983
#line 6985
    [DIFFICULTY_EASY][TRAINER_RIVETSHORE_GYM_C] =
    {
#line 6984
        .trainerName = _("Babeneitor"),
#line 6986
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 6987
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 6989
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 6990
        .doubleBattle = FALSE,
#line 6991
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 6993
            .species = SPECIES_ARCANINE_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 6993
            .heldItem = ITEM_FOCUS_SASH,
#line 6997
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 6994
            .ability = ABILITY_ROCK_HEAD,
#line 6996
            .lvl = 47,
#line 6995
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 6998
                MOVE_HEAD_SMASH,
                MOVE_FLARE_BLITZ,
                MOVE_EXTREME_SPEED,
                MOVE_WILD_CHARGE,
            },
            },
        },
    },
#line 7004
#line 7006
    [DIFFICULTY_NORMAL][TRAINER_RIVETSHORE_GYM_C] =
    {
#line 7005
        .trainerName = _("Babeneitor"),
#line 7007
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 7008
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 7010
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 7011
        .doubleBattle = FALSE,
#line 7012
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 7014
            .species = SPECIES_ARCANINE_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7014
            .heldItem = ITEM_FOCUS_SASH,
#line 7018
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7015
            .ability = ABILITY_ROCK_HEAD,
#line 7017
            .lvl = 47,
#line 7016
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 7018
                MOVE_HEAD_SMASH,
                MOVE_FLARE_BLITZ,
                MOVE_EXTREME_SPEED,
                MOVE_WILD_CHARGE,
            },
            },
        },
    },
#line 7036
#line 7038
    [DIFFICULTY_EASY][TRAINER_RIVETSHORE_GYM_D] =
    {
#line 7037
        .trainerName = _("Roland"),
#line 7039
        .trainerClass = TRAINER_CLASS_BUILDER,
#line 7040
        .trainerPic = TRAINER_PIC_BUILDER,
        .encounterMusic_gender =
#line 7042
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7043
        .doubleBattle = FALSE,
#line 7044
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7046
            .species = SPECIES_REVAVROOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7048
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 7047
            .lvl = 45,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7050
            .species = SPECIES_LAIRON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7052
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 7051
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7054
#line 7056
    [DIFFICULTY_NORMAL][TRAINER_RIVETSHORE_GYM_D] =
    {
#line 7055
        .trainerName = _("Roland"),
#line 7057
        .trainerClass = TRAINER_CLASS_BUILDER,
#line 7058
        .trainerPic = TRAINER_PIC_BUILDER,
        .encounterMusic_gender =
#line 7060
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7061
        .doubleBattle = FALSE,
#line 7062
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7064
            .species = SPECIES_REVAVROOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7066
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7065
            .lvl = 45,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7067
            .species = SPECIES_LAIRON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7069
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7068
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7082
#line 7084
    [DIFFICULTY_EASY][TRAINER_RIVETSHORE_GYM_E] =
    {
#line 7083
        .trainerName = _("Nolen"),
#line 7085
        .trainerClass = TRAINER_CLASS_HIKER,
#line 7086
        .trainerPic = TRAINER_PIC_HIKER,
        .encounterMusic_gender =
#line 7088
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7089
        .doubleBattle = FALSE,
#line 7090
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7092
            .species = SPECIES_GLIMMET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7094
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 7093
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7096
            .species = SPECIES_CARKOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7098
            .iv = TRAINER_PARTY_IVS(20, 20, 20, 20, 20, 20),
#line 7097
            .lvl = 48,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7100
#line 7102
    [DIFFICULTY_NORMAL][TRAINER_RIVETSHORE_GYM_E] =
    {
#line 7101
        .trainerName = _("Nolen"),
#line 7103
        .trainerClass = TRAINER_CLASS_HIKER,
#line 7104
        .trainerPic = TRAINER_PIC_HIKER,
        .encounterMusic_gender =
#line 7106
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7107
        .doubleBattle = FALSE,
#line 7108
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7110
            .species = SPECIES_GLIMMORA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7110
            .heldItem = ITEM_POWER_HERB,
#line 7112
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7111
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7113
            .species = SPECIES_COALOSSAL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7113
            .heldItem = ITEM_PASSHO_BERRY,
#line 7115
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7114
            .lvl = 48,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7127
#line 7129
    [DIFFICULTY_EASY][TRAINER_SSELEGANT_A] =
    {
#line 7128
        .trainerName = _("Adario"),
#line 7130
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 7131
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 7133
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 7134
        .doubleBattle = FALSE,
#line 7135
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 7137
            .species = SPECIES_CLODSIRE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7139
            .iv = TRAINER_PARTY_IVS(23, 23, 23, 23, 23, 23),
#line 7138
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7141
            .species = SPECIES_DHELMISE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7143
            .iv = TRAINER_PARTY_IVS(23, 23, 23, 23, 23, 23),
#line 7142
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7145
            .species = SPECIES_MORGREM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7147
            .iv = TRAINER_PARTY_IVS(23, 23, 23, 23, 23, 23),
#line 7146
            .lvl = 49,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7149
#line 7151
    [DIFFICULTY_NORMAL][TRAINER_SSELEGANT_A] =
    {
#line 7150
        .trainerName = _("Adario"),
#line 7152
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 7153
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 7155
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 7156
        .doubleBattle = FALSE,
#line 7157
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 7159
            .species = SPECIES_CLODSIRE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7161
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7160
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7162
            .species = SPECIES_DHELMISE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7164
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7163
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7165
            .species = SPECIES_MORGREM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7167
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7166
            .lvl = 49,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7180
#line 7182
    [DIFFICULTY_EASY][TRAINER_SSELEGANT_B] =
    {
#line 7181
        .trainerName = _("BARRY"),
#line 7183
        .trainerClass = TRAINER_CLASS_SWIMMER_M,
#line 7184
        .trainerPic = TRAINER_PIC_SWIMMER_M,
        .encounterMusic_gender =
#line 7186
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7187
        .doubleBattle = FALSE,
#line 7188
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 7190
            .species = SPECIES_GYARADOS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7192
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 7191
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7205
#line 7207
    [DIFFICULTY_EASY][TRAINER_SSELEGANT_INGER] =
    {
#line 7206
        .trainerName = _("Inger"),
#line 7208
        .trainerClass = TRAINER_CLASS_LEADER,
#line 7209
        .trainerPic = TRAINER_PIC_LEADER_INGER,
        .encounterMusic_gender =
#line 7210
F_TRAINER_FEMALE | 
#line 7211
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 7214
        .items = { ITEM_HYPER_POTION },
#line 7212
        .doubleBattle = FALSE,
#line 7213
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 7216
            .species = SPECIES_LYCANROC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7218
            .iv = TRAINER_PARTY_IVS(23, 23, 23, 23, 23, 23),
#line 7217
            .lvl = 45,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7220
            .species = SPECIES_GOLEM_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7220
            .heldItem = ITEM_LEFTOVERS,
#line 7222
            .iv = TRAINER_PARTY_IVS(23, 23, 23, 23, 23, 23),
#line 7221
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7224
            .species = SPECIES_MINIOR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7224
            .heldItem = ITEM_SITRUS_BERRY,
#line 7226
            .iv = TRAINER_PARTY_IVS(23, 23, 23, 23, 23, 23),
#line 7225
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7228
#line 7230
    [DIFFICULTY_NORMAL][TRAINER_SSELEGANT_INGER] =
    {
#line 7229
        .trainerName = _("Inger"),
#line 7231
        .trainerClass = TRAINER_CLASS_LEADER,
#line 7232
        .trainerPic = TRAINER_PIC_LEADER_INGER,
        .encounterMusic_gender =
#line 7233
F_TRAINER_FEMALE | 
#line 7234
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 7237
        .items = { ITEM_HYPER_POTION },
#line 7235
        .doubleBattle = FALSE,
#line 7236
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 7239
            .species = SPECIES_LYCANROC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7241
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7240
            .lvl = 45,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7242
            .species = SPECIES_GOLEM_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7242
            .heldItem = ITEM_LEFTOVERS,
#line 7244
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7243
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7245
            .species = SPECIES_MINIOR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7245
            .heldItem = ITEM_SITRUS_BERRY,
#line 7247
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7246
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7259
#line 7261
    [DIFFICULTY_EASY][TRAINER_SSELEGANT_ARIANA] =
    {
#line 7260
        .trainerName = _("Ariana"),
#line 7262
        .trainerClass = TRAINER_CLASS_LEADER,
#line 7263
        .trainerPic = TRAINER_PIC_LEADER_ARIANA,
        .encounterMusic_gender =
#line 7265
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 7266
        .items = { ITEM_SUPER_POTION },
#line 7267
        .doubleBattle = FALSE,
#line 7268
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 7270
            .species = SPECIES_TALONFLAME,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7272
            .iv = TRAINER_PARTY_IVS(23, 23, 23, 23, 23, 23),
#line 7271
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7274
            .species = SPECIES_CENTISKORCH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7276
            .iv = TRAINER_PARTY_IVS(23, 23, 23, 23, 23, 23),
#line 7275
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7278
            .species = SPECIES_TAUROS_PALDEA_BLAZE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7280
            .iv = TRAINER_PARTY_IVS(23, 23, 23, 23, 23, 23),
#line 7279
            .lvl = 49,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7282
#line 7284
    [DIFFICULTY_NORMAL][TRAINER_SSELEGANT_ARIANA] =
    {
#line 7283
        .trainerName = _("Ariana"),
#line 7285
        .trainerClass = TRAINER_CLASS_LEADER,
#line 7286
        .trainerPic = TRAINER_PIC_LEADER_ARIANA,
        .encounterMusic_gender =
#line 7288
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 7289
        .items = { ITEM_SUPER_POTION },
#line 7290
        .doubleBattle = FALSE,
#line 7291
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 7293
            .species = SPECIES_TALONFLAME,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7295
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7294
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7296
            .species = SPECIES_CENTISKORCH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7298
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7297
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7299
            .species = SPECIES_TAUROS_PALDEA_BLAZE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7301
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7300
            .lvl = 49,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7314
#line 7316
    [DIFFICULTY_EASY][TRAINER_SSELEGANT_JANIA] =
    {
#line 7315
        .trainerName = _("Jania"),
#line 7317
        .trainerClass = TRAINER_CLASS_ARTIST,
#line 7318
        .trainerPic = TRAINER_PIC_JANIA_ARTIST,
        .encounterMusic_gender =
#line 7319
F_TRAINER_FEMALE | 
#line 7320
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7321
        .doubleBattle = FALSE,
#line 7322
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7324
            .species = SPECIES_SMEARGLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7326
            .iv = TRAINER_PARTY_IVS(23, 23, 23, 23, 23, 23),
#line 7325
            .lvl = 48,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7328
            .species = SPECIES_CLAWITZER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7330
            .iv = TRAINER_PARTY_IVS(23, 23, 23, 23, 23, 23),
#line 7329
            .lvl = 50,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7332
#line 7334
    [DIFFICULTY_NORMAL][TRAINER_SSELEGANT_JANIA] =
    {
#line 7333
        .trainerName = _("Jania"),
#line 7335
        .trainerClass = TRAINER_CLASS_ARTIST,
#line 7336
        .trainerPic = TRAINER_PIC_JANIA_ARTIST,
        .encounterMusic_gender =
#line 7337
F_TRAINER_FEMALE | 
#line 7338
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7339
        .doubleBattle = TRUE,
#line 7340
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7342
            .species = SPECIES_SMEARGLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7342
            .heldItem = ITEM_LEFTOVERS,
#line 7344
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7343
            .lvl = 48,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7345
            .species = SPECIES_CLAWITZER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7345
            .heldItem = ITEM_CHOICE_SPECS,
#line 7347
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7346
            .lvl = 50,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7362
#line 7364
    [DIFFICULTY_EASY][TRAINER_RIVETSHORE_GYM_LEADER] =
    {
#line 7363
        .trainerName = _("Raazi"),
#line 7365
        .trainerClass = TRAINER_CLASS_LEADER,
#line 7366
        .trainerPic = TRAINER_PIC_LEADER_RAAZI,
        .encounterMusic_gender =
#line 7368
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7370
        .items = { ITEM_FULL_RESTORE },
#line 7369
        .doubleBattle = FALSE,
#line 7371
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 7372
        .mugshotColor = MUGSHOT_COLOR_BLUE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 7374
            .species = SPECIES_DUGTRIO_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7376
            .iv = TRAINER_PARTY_IVS(24, 24, 24, 24, 24, 24),
#line 7375
            .lvl = 48,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7378
            .species = SPECIES_SKARMORY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7380
            .iv = TRAINER_PARTY_IVS(24, 24, 24, 24, 24, 24),
#line 7379
            .lvl = 50,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 7381
                MOVE_STEEL_WING,
                MOVE_DRILL_PECK,
                MOVE_ROOST,
            },
            },
            {
#line 7385
            .species = SPECIES_EXCADRILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7387
            .iv = TRAINER_PARTY_IVS(24, 24, 24, 24, 24, 24),
#line 7386
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7389
            .species = SPECIES_COALOSSAL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7391
            .iv = TRAINER_PARTY_IVS(24, 24, 24, 24, 24, 24),
#line 7390
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7393
            .species = SPECIES_AGGRON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7393
            .heldItem = ITEM_AGGRONITE,
#line 7395
            .iv = TRAINER_PARTY_IVS(24, 24, 24, 24, 24, 24),
#line 7394
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7397
#line 7399
    [DIFFICULTY_NORMAL][TRAINER_RIVETSHORE_GYM_LEADER] =
    {
#line 7398
        .trainerName = _("Raazi"),
#line 7400
        .trainerClass = TRAINER_CLASS_LEADER,
#line 7401
        .trainerPic = TRAINER_PIC_LEADER_RAAZI,
        .encounterMusic_gender =
#line 7403
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7405
        .items = { ITEM_FULL_RESTORE },
#line 7404
        .doubleBattle = FALSE,
#line 7406
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 7407
        .mugshotColor = MUGSHOT_COLOR_BLUE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 7409
            .species = SPECIES_DUGTRIO_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7411
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7410
            .lvl = 48,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7412
            .species = SPECIES_SKARMORY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7415
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7414
            .ability = ABILITY_WEAK_ARMOR,
#line 7413
            .lvl = 50,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 7415
                MOVE_BODY_PRESS,
                MOVE_DRILL_PECK,
                MOVE_ROOST,
                MOVE_IRON_DEFENSE,
            },
            },
            {
#line 7420
            .species = SPECIES_EXCADRILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7422
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7421
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7423
            .species = SPECIES_COALOSSAL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7425
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7424
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7426
            .species = SPECIES_AGGRON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7426
            .heldItem = ITEM_AGGRONITE,
#line 7428
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7427
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7439
#line 7441
    [DIFFICULTY_EASY][TRAINER_IVY_RIVER_A] =
    {
#line 7440
        .trainerName = _("Santiago"),
#line 7442
        .trainerClass = TRAINER_CLASS_RUIN_MANIAC,
#line 7443
        .trainerPic = TRAINER_PIC_RUIN_MANIAC,
        .encounterMusic_gender =
#line 7445
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 7446
        .doubleBattle = FALSE,
#line 7447
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7449
            .species = SPECIES_BOMBIRDIER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7451
            .iv = TRAINER_PARTY_IVS(18, 18, 18, 18, 18, 18),
#line 7450
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7453
            .species = SPECIES_METANG,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7455
            .iv = TRAINER_PARTY_IVS(18, 18, 18, 18, 18, 18),
#line 7454
            .lvl = 38,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7457
#line 7459
    [DIFFICULTY_NORMAL][TRAINER_IVY_RIVER_A] =
    {
#line 7458
        .trainerName = _("Santiago"),
#line 7460
        .trainerClass = TRAINER_CLASS_RUIN_MANIAC,
#line 7461
        .trainerPic = TRAINER_PIC_RUIN_MANIAC,
        .encounterMusic_gender =
#line 7463
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 7464
        .doubleBattle = FALSE,
#line 7465
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7467
            .species = SPECIES_BOMBIRDIER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7469
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7468
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7470
            .species = SPECIES_METANG,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7472
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7471
            .lvl = 38,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7484
#line 7486
    [DIFFICULTY_EASY][TRAINER_IVY_RIVER_B] =
    {
#line 7485
        .trainerName = _("Galona"),
#line 7487
        .trainerClass = TRAINER_CLASS_SWIMMER_F,
#line 7488
        .trainerPic = TRAINER_PIC_SWIMMER_F,
        .encounterMusic_gender =
#line 7489
F_TRAINER_FEMALE | 
#line 7490
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7491
        .doubleBattle = FALSE,
#line 7492
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7494
            .species = SPECIES_TYNAMO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7496
            .iv = TRAINER_PARTY_IVS(18, 18, 18, 18, 18, 18),
#line 7495
            .lvl = 37,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7498
            .species = SPECIES_CARVANHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7500
            .iv = TRAINER_PARTY_IVS(18, 18, 18, 18, 18, 18),
#line 7499
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7502
#line 7504
    [DIFFICULTY_NORMAL][TRAINER_IVY_RIVER_B] =
    {
#line 7503
        .trainerName = _("Galona"),
#line 7505
        .trainerClass = TRAINER_CLASS_SWIMMER_F,
#line 7506
        .trainerPic = TRAINER_PIC_SWIMMER_F,
        .encounterMusic_gender =
#line 7507
F_TRAINER_FEMALE | 
#line 7508
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7509
        .doubleBattle = FALSE,
#line 7510
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7512
            .species = SPECIES_TYNAMO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7514
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7513
            .lvl = 37,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7515
            .species = SPECIES_CARVANHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7517
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7516
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7530
#line 7532
    [DIFFICULTY_EASY][TRAINER_IVY_RIVER_C] =
    {
#line 7531
        .trainerName = _("Eden"),
#line 7533
        .trainerClass = TRAINER_CLASS_HEX_MANIAC,
#line 7534
        .trainerPic = TRAINER_PIC_HEX_MANIAC,
        .encounterMusic_gender =
#line 7535
F_TRAINER_FEMALE | 
#line 7536
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 7537
        .doubleBattle = FALSE,
#line 7538
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_FORCE_SETUP_FIRST_TURN,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 7540
            .species = SPECIES_MORGREM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7540
            .heldItem = ITEM_LAGGING_TAIL,
#line 7543
            .iv = TRAINER_PARTY_IVS(18, 18, 18, 18, 18, 18),
#line 7542
            .ability = ABILITY_PRANKSTER,
#line 7541
            .lvl = 37,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 7544
                MOVE_TRICK,
                MOVE_PARTING_SHOT,
                MOVE_FAKE_OUT,
                MOVE_SUCKER_PUNCH,
            },
            },
            {
#line 7549
            .species = SPECIES_POLTEAGEIST,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7552
            .iv = TRAINER_PARTY_IVS(18, 18, 18, 18, 18, 18),
#line 7551
            .ability = ABILITY_WEAK_ARMOR,
#line 7550
            .lvl = 38,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 7553
                MOVE_STRENGTH_SAP,
                MOVE_NASTY_PLOT,
                MOVE_BATON_PASS,
                MOVE_ENDURE,
            },
            },
            {
#line 7558
            .species = SPECIES_SPIRITOMB,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7561
            .iv = TRAINER_PARTY_IVS(18, 18, 18, 18, 18, 18),
#line 7560
            .ability = ABILITY_INFILTRATOR,
#line 7559
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 7562
                MOVE_FOUL_PLAY,
                MOVE_WILL_O_WISP,
                MOVE_HEX,
                MOVE_PAIN_SPLIT,
            },
            },
        },
    },
#line 7567
#line 7569
    [DIFFICULTY_NORMAL][TRAINER_IVY_RIVER_C] =
    {
#line 7568
        .trainerName = _("Eden"),
#line 7570
        .trainerClass = TRAINER_CLASS_HEX_MANIAC,
#line 7571
        .trainerPic = TRAINER_PIC_HEX_MANIAC,
        .encounterMusic_gender =
#line 7572
F_TRAINER_FEMALE | 
#line 7573
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 7574
        .doubleBattle = FALSE,
#line 7575
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_FORCE_SETUP_FIRST_TURN,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 7577
            .species = SPECIES_MORGREM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7577
            .heldItem = ITEM_LAGGING_TAIL,
#line 7580
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7579
            .ability = ABILITY_PRANKSTER,
#line 7578
            .lvl = 37,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 7580
                MOVE_TRICK,
                MOVE_PARTING_SHOT,
                MOVE_FAKE_OUT,
                MOVE_SUCKER_PUNCH,
            },
            },
            {
#line 7585
            .species = SPECIES_POLTEAGEIST,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7588
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7587
            .ability = ABILITY_WEAK_ARMOR,
#line 7586
            .lvl = 38,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 7588
                MOVE_STRENGTH_SAP,
                MOVE_NASTY_PLOT,
                MOVE_BATON_PASS,
                MOVE_ENDURE,
            },
            },
            {
#line 7593
            .species = SPECIES_SPIRITOMB,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7596
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7595
            .ability = ABILITY_INFILTRATOR,
#line 7594
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 7596
                MOVE_FOUL_PLAY,
                MOVE_WILL_O_WISP,
                MOVE_HEX,
                MOVE_PAIN_SPLIT,
            },
            },
        },
    },
#line 7613
#line 7615
    [DIFFICULTY_EASY][TRAINER_IVY_RIVER_D] =
    {
#line 7614
        .trainerName = _("Stanja"),
#line 7616
        .trainerClass = TRAINER_CLASS_BUG_MANIAC,
#line 7617
        .trainerPic = TRAINER_PIC_BUG_MANIAC,
        .encounterMusic_gender =
#line 7619
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7620
        .doubleBattle = FALSE,
#line 7621
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 7622
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 7624
            .species = SPECIES_GLIMMORA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7626
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 7625
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7628
            .species = SPECIES_DEWPIDER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7630
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 7629
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7632
            .species = SPECIES_MAREANIE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7634
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 7633
            .lvl = 37,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7636
            .species = SPECIES_PINSIR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7638
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 7637
            .lvl = 40,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7640
#line 7642
    [DIFFICULTY_NORMAL][TRAINER_IVY_RIVER_D] =
    {
#line 7641
        .trainerName = _("Stanja"),
#line 7643
        .trainerClass = TRAINER_CLASS_BUG_MANIAC,
#line 7644
        .trainerPic = TRAINER_PIC_BUG_MANIAC,
        .encounterMusic_gender =
#line 7646
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7647
        .doubleBattle = FALSE,
#line 7648
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 7649
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 7651
            .species = SPECIES_GLIMMORA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7653
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7652
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7654
            .species = SPECIES_DEWPIDER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7656
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7655
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7657
            .species = SPECIES_MAREANIE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7659
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7658
            .lvl = 37,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7660
            .species = SPECIES_PINSIR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7662
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7661
            .lvl = 40,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7674
#line 7676
    [DIFFICULTY_EASY][TRAINER_UNCHARTED_ISLAND_GRUNT_A] =
    {
#line 7675
        .trainerName = _("Grunt"),
#line 7677
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 7678
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 7680
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 7681
        .doubleBattle = FALSE,
#line 7682
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 7684
            .species = SPECIES_MUK_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7686
            .iv = TRAINER_PARTY_IVS(23, 23, 23, 23, 23, 23),
#line 7685
            .lvl = 48,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7688
#line 7690
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_A] =
    {
#line 7689
        .trainerName = _("Grunt"),
#line 7691
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 7692
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 7694
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 7695
        .doubleBattle = FALSE,
#line 7696
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 7698
            .species = SPECIES_MUK_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7700
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7699
            .lvl = 48,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7711
#line 7713
    [DIFFICULTY_EASY][TRAINER_UNCHARTED_ISLAND_GRUNT_B] =
    {
#line 7712
        .trainerName = _("Grunt"),
#line 7714
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 7715
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 7717
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 7718
        .doubleBattle = FALSE,
#line 7719
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7721
            .species = SPECIES_YANMEGA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7723
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 7722
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7725
            .species = SPECIES_BRONZONG,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7727
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 7726
            .lvl = 48,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7729
#line 7731
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_B] =
    {
#line 7730
        .trainerName = _("Grunt"),
#line 7732
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 7733
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 7735
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 7736
        .doubleBattle = FALSE,
#line 7737
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7739
            .species = SPECIES_YANMEGA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7741
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7740
            .lvl = 46,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7742
            .species = SPECIES_BRONZONG,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7744
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7743
            .lvl = 48,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7756
#line 7758
    [DIFFICULTY_EASY][TRAINER_UNCHARTED_ISLAND_GRUNT_C] =
    {
#line 7757
        .trainerName = _("Grunt"),
#line 7759
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 7760
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 7762
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 7763
        .doubleBattle = FALSE,
#line 7764
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7766
            .species = SPECIES_HONCHKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7768
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 7767
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7770
            .species = SPECIES_HYPNO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7772
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 7771
            .lvl = 48,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7774
#line 7776
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_C] =
    {
#line 7775
        .trainerName = _("Grunt"),
#line 7777
        .trainerClass = TRAINER_CLASS_TEAM_SOMBER,
#line 7778
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_M,
        .encounterMusic_gender =
#line 7780
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 7781
        .doubleBattle = FALSE,
#line 7782
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 7784
            .species = SPECIES_HONCHKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7786
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7785
            .lvl = 47,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7787
            .species = SPECIES_HYPNO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7789
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7788
            .lvl = 48,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7801
#line 7803
    [DIFFICULTY_EASY][TRAINER_UNCHARTED_ISLAND_GRUNT_D] =
    {
#line 7802
        .trainerName = _("Tony"),
#line 7804
        .trainerClass = TRAINER_CLASS_SWIMMER_M,
#line 7805
        .trainerPic = TRAINER_PIC_SWIMMER_M,
        .encounterMusic_gender =
#line 7807
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7808
        .doubleBattle = FALSE,
#line 7809
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 7811
            .species = SPECIES_SHARPEDO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7813
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 7812
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7815
#line 7817
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_D] =
    {
#line 7816
        .trainerName = _("Tony"),
#line 7818
        .trainerClass = TRAINER_CLASS_SWIMMER_M,
#line 7819
        .trainerPic = TRAINER_PIC_SWIMMER_M,
        .encounterMusic_gender =
#line 7821
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7822
        .doubleBattle = FALSE,
#line 7823
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 7825
            .species = SPECIES_SHARPEDO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7827
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7826
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7840
#line 7842
    [DIFFICULTY_EASY][TRAINER_UNCHARTED_ISLAND_MOXIE] =
    {
#line 7841
        .trainerName = _("Moxie"),
#line 7843
        .trainerClass = TRAINER_CLASS_SOMBER_ADMIN,
#line 7844
        .trainerPic = TRAINER_PIC_SOMBER_ADMIN_MOXIE,
        .encounterMusic_gender =
#line 7846
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 7847
        .items = { ITEM_HYPER_POTION },
#line 7848
        .doubleBattle = FALSE,
#line 7849
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 7850
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 7852
            .species = SPECIES_GRIMMSNARL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7854
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 7853
            .lvl = 49,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7856
            .species = SPECIES_HONCHKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7858
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 7857
            .lvl = 50,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7860
            .species = SPECIES_SLOWKING_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7862
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 7861
            .lvl = 50,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7864
            .species = SPECIES_GREAT_TUSK,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7866
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 7865
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7868
            .species = SPECIES_HOUNDOOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7868
            .heldItem = ITEM_HOUNDOOMINITE,
#line 7870
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 7869
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7872
#line 7874
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_MOXIE] =
    {
#line 7873
        .trainerName = _("Moxie"),
#line 7875
        .trainerClass = TRAINER_CLASS_SOMBER_ADMIN,
#line 7876
        .trainerPic = TRAINER_PIC_SOMBER_ADMIN_MOXIE,
        .encounterMusic_gender =
#line 7878
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 7879
        .items = { ITEM_FULL_RESTORE },
#line 7880
        .doubleBattle = FALSE,
#line 7881
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 7882
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 7884
            .species = SPECIES_GRIMMSNARL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7886
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7885
            .lvl = 49,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7887
            .species = SPECIES_HONCHKROW,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7889
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7888
            .lvl = 50,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7890
            .species = SPECIES_SLOWKING_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7892
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7891
            .lvl = 50,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7893
            .species = SPECIES_GREAT_TUSK,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7895
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7894
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7896
            .species = SPECIES_HOUNDOOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7896
            .heldItem = ITEM_HOUNDOOMINITE,
#line 7898
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7897
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7913
#line 7915
    [DIFFICULTY_EASY][TRAINER_UNCHARTED_ISLAND_MELEA] =
    {
#line 7914
        .trainerName = _("Melea"),
#line 7916
        .trainerClass = TRAINER_CLASS_SOMBER_ADMIN,
#line 7917
        .trainerPic = TRAINER_PIC_SOMBER_ADMIN_MELEA,
        .encounterMusic_gender =
#line 7918
F_TRAINER_FEMALE | 
#line 7919
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 7920
        .doubleBattle = FALSE,
#line 7921
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 7922
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 7924
            .species = SPECIES_YANMEGA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7926
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 7925
            .lvl = 50,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7928
            .species = SPECIES_MUK_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7930
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 7929
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7932
            .species = SPECIES_SLOWBRO_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7934
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 7933
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7936
            .species = SPECIES_FLUTTER_MANE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7938
            .iv = TRAINER_PARTY_IVS(15, 25, 15, 25, 25, 15),
#line 7937
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7940
            .species = SPECIES_ABSOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7940
            .heldItem = ITEM_ABSOLITE,
#line 7942
            .iv = TRAINER_PARTY_IVS(25, 25, 25, 25, 25, 25),
#line 7941
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7944
#line 7946
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_MELEA] =
    {
#line 7945
        .trainerName = _("Melea"),
#line 7947
        .trainerClass = TRAINER_CLASS_SOMBER_ADMIN,
#line 7948
        .trainerPic = TRAINER_PIC_SOMBER_ADMIN_MELEA,
        .encounterMusic_gender =
#line 7949
F_TRAINER_FEMALE | 
#line 7950
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 7951
        .doubleBattle = FALSE,
#line 7952
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 7953
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 7955
            .species = SPECIES_YANMEGA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7957
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7956
            .lvl = 50,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7958
            .species = SPECIES_MUK_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7960
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7959
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7961
            .species = SPECIES_SLOWBRO_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7963
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7962
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7964
            .species = SPECIES_FLUTTER_MANE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7966
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7965
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7967
            .species = SPECIES_ABSOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7967
            .heldItem = ITEM_ABSOLITE,
#line 7969
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7968
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 7981
#line 7983
    [DIFFICULTY_EASY][TRAINER_UNCHARTED_ISLAND_RUE] =
    {
#line 7982
        .trainerName = _("Rue"),
#line 7984
        .trainerClass = TRAINER_CLASS_RUE,
#line 7985
        .trainerPic = TRAINER_PIC_RUE,
        .encounterMusic_gender =
#line 7987
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 7988
        .doubleBattle = FALSE,
#line 7989
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 7990
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 7992
            .species = SPECIES_TOEDSCRUEL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7994
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7993
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7995
            .species = SPECIES_SPIRITOMB,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 7997
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7996
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 7998
            .species = SPECIES_ROARING_MOON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8000
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 7999
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8001
            .species = SPECIES_METAGROSS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8001
            .heldItem = ITEM_METAGROSSITE,
#line 8003
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8002
            .lvl = 55,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8004
            .species = SPECIES_KORAIDON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8006
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8005
            .lvl = 56,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8007
#line 8009
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_RUE] =
    {
#line 8008
        .trainerName = _("Rue"),
#line 8010
        .trainerClass = TRAINER_CLASS_RUE,
#line 8011
        .trainerPic = TRAINER_PIC_RUE,
        .encounterMusic_gender =
#line 8013
            TRAINER_ENCOUNTER_MUSIC_SWIMMER,
#line 8014
        .doubleBattle = FALSE,
#line 8015
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 8016
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 8018
            .species = SPECIES_TOEDSCRUEL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8020
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8019
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8021
            .species = SPECIES_SPIRITOMB,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8023
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8022
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8024
            .species = SPECIES_ROARING_MOON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8026
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8025
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8027
            .species = SPECIES_METAGROSS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8027
            .heldItem = ITEM_METAGROSSITE,
#line 8029
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8028
            .lvl = 55,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8030
            .species = SPECIES_KORAIDON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8032
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8031
            .lvl = 56,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8043
#line 8045
    [DIFFICULTY_EASY][TRAINER_ROUTE1_STRONG_A] =
    {
#line 8044
        .trainerName = _("Jose"),
#line 8046
        .trainerClass = TRAINER_CLASS_YOUNGSTER,
#line 8047
        .trainerPic = TRAINER_PIC_YOUNGSTER,
        .encounterMusic_gender =
#line 8049
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 8050
        .doubleBattle = FALSE,
#line 8051
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8053
            .species = SPECIES_MAROWAK_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8055
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8054
            .lvl = 50,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8057
            .species = SPECIES_RATICATE_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8059
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8058
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8061
#line 8063
    [DIFFICULTY_NORMAL][TRAINER_ROUTE1_STRONG_A] =
    {
#line 8062
        .trainerName = _("Jose"),
#line 8064
        .trainerClass = TRAINER_CLASS_YOUNGSTER,
#line 8065
        .trainerPic = TRAINER_PIC_YOUNGSTER,
        .encounterMusic_gender =
#line 8067
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 8068
        .doubleBattle = FALSE,
#line 8069
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_RISKY,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8071
            .species = SPECIES_MAROWAK_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8073
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8072
            .lvl = 50,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8074
            .species = SPECIES_RATICATE_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8076
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8075
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8088
#line 8090
    [DIFFICULTY_EASY][TRAINER_ROUTE1_STRONG_B] =
    {
#line 8089
        .trainerName = _("Sana"),
#line 8091
        .trainerClass = TRAINER_CLASS_LASS,
#line 8092
        .trainerPic = TRAINER_PIC_LASS,
        .encounterMusic_gender =
#line 8093
F_TRAINER_FEMALE | 
#line 8094
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 8095
        .doubleBattle = FALSE,
#line 8096
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 8098
            .species = SPECIES_NOIVERN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8100
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8099
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8102
            .species = SPECIES_PELIPPER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8104
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8103
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8106
            .species = SPECIES_UNFEZANT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8108
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8107
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8110
#line 8112
    [DIFFICULTY_NORMAL][TRAINER_ROUTE1_STRONG_B] =
    {
#line 8111
        .trainerName = _("Sana"),
#line 8113
        .trainerClass = TRAINER_CLASS_LASS,
#line 8114
        .trainerPic = TRAINER_PIC_LASS,
        .encounterMusic_gender =
#line 8115
F_TRAINER_FEMALE | 
#line 8116
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 8117
        .doubleBattle = FALSE,
#line 8118
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 8120
            .species = SPECIES_NOIVERN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8122
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8121
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8124
            .species = SPECIES_PELIPPER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8126
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8125
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8128
            .species = SPECIES_UNFEZANT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8130
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8129
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8144
#line 8146
    [DIFFICULTY_EASY][TRAINER_ROUTE1_STRONG_C] =
    {
#line 8145
        .trainerName = _("Manya"),
#line 8147
        .trainerClass = TRAINER_CLASS_BUG_CATCHER_F,
#line 8148
        .trainerPic = TRAINER_PIC_BUG_CATCHER_F,
        .encounterMusic_gender =
#line 8150
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 8151
        .doubleBattle = FALSE,
#line 8152
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8154
            .species = SPECIES_ORBEETLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8156
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8155
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8158
            .species = SPECIES_LOKIX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8160
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8159
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8162
#line 8164
    [DIFFICULTY_NORMAL][TRAINER_ROUTE1_STRONG_C] =
    {
#line 8163
        .trainerName = _("Manya"),
#line 8165
        .trainerClass = TRAINER_CLASS_BUG_CATCHER_F,
#line 8166
        .trainerPic = TRAINER_PIC_BUG_CATCHER_F,
        .encounterMusic_gender =
#line 8168
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 8169
        .doubleBattle = FALSE,
#line 8170
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8172
            .species = SPECIES_ORBEETLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8174
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8173
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8176
            .species = SPECIES_LOKIX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8178
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8177
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8192
#line 8194
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_A] =
    {
#line 8193
        .trainerName = _("Koichi"),
#line 8195
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 8196
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 8198
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8199
        .doubleBattle = FALSE,
#line 8200
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 8202
            .species = SPECIES_SINISTEA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8204
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8203
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8206
            .species = SPECIES_ARAQUANID,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8208
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8207
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8210
            .species = SPECIES_COALOSSAL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8212
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8211
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8214
#line 8216
    [DIFFICULTY_NORMAL][TRAINER_VICTORY_ROAD_A] =
    {
#line 8215
        .trainerName = _("Koichi"),
#line 8217
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 8218
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 8220
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8221
        .doubleBattle = FALSE,
#line 8222
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 8224
            .species = SPECIES_SINISTEA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8226
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8225
            .lvl = 51,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8228
            .species = SPECIES_ARAQUANID,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8230
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8229
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8232
            .species = SPECIES_COALOSSAL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8234
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8233
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8249
#line 8251
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_B] =
    {
#line 8250
        .trainerName = _("Sari"),
#line 8252
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 8253
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 8255
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8256
        .doubleBattle = FALSE,
#line 8257
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8259
            .species = SPECIES_TOXTRICITY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8261
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8260
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8263
            .species = SPECIES_SEISMITOAD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8265
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8264
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8267
#line 8269
    [DIFFICULTY_NORMAL][TRAINER_VICTORY_ROAD_B] =
    {
#line 8268
        .trainerName = _("Sari"),
#line 8270
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 8271
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 8273
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8274
        .doubleBattle = FALSE,
#line 8275
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8277
            .species = SPECIES_TOXTRICITY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8279
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8278
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8281
            .species = SPECIES_SEISMITOAD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8283
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8282
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8298
#line 8300
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_C] =
    {
#line 8299
        .trainerName = _("Gorbygorb"),
#line 8301
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 8302
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 8304
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8305
        .doubleBattle = FALSE,
#line 8306
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 8308
            .species = SPECIES_MEDICHAM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8310
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8309
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 8311
                MOVE_ICE_PUNCH,
                MOVE_THUNDER_PUNCH,
                MOVE_ZEN_HEADBUTT,
                MOVE_AXE_KICK,
            },
            },
            {
#line 8316
            .species = SPECIES_MEGANIUM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8316
            .heldItem = ITEM_LEFTOVERS,
#line 8318
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8317
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 8319
                MOVE_BODY_SLAM,
                MOVE_LEECH_SEED,
                MOVE_GIGA_DRAIN,
                MOVE_COUNTER,
            },
            },
            {
#line 8324
            .species = SPECIES_ALTARIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8326
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8325
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 8326
                MOVE_DRAGON_DANCE,
                MOVE_OUTRAGE,
                MOVE_ACROBATICS,
                MOVE_EARTHQUAKE,
            },
            },
            {
#line 8331
            .species = SPECIES_BASCULIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8331
            .heldItem = ITEM_CHOICE_BAND,
#line 8334
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8333
            .ability = ABILITY_ADAPTABILITY,
#line 8332
            .lvl = 55,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 8335
                MOVE_WAVE_CRASH,
                MOVE_AQUA_JET,
                MOVE_HEAD_SMASH,
                MOVE_CRUNCH,
            },
            },
        },
    },
#line 8340
#line 8342
    [DIFFICULTY_NORMAL][TRAINER_VICTORY_ROAD_C] =
    {
#line 8341
        .trainerName = _("Gorbygorb"),
#line 8343
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 8344
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 8346
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8347
        .doubleBattle = FALSE,
#line 8348
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 8350
            .species = SPECIES_MEDICHAM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8352
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8351
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 8353
                MOVE_ICE_PUNCH,
                MOVE_THUNDER_PUNCH,
                MOVE_ZEN_HEADBUTT,
                MOVE_AXE_KICK,
            },
            },
            {
#line 8358
            .species = SPECIES_MEGANIUM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8358
            .heldItem = ITEM_LEFTOVERS,
#line 8360
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8359
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 8361
                MOVE_BODY_SLAM,
                MOVE_LEECH_SEED,
                MOVE_GIGA_DRAIN,
                MOVE_COUNTER,
            },
            },
            {
#line 8366
            .species = SPECIES_ALTARIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8368
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8367
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 8368
                MOVE_DRAGON_DANCE,
                MOVE_OUTRAGE,
                MOVE_ACROBATICS,
                MOVE_EARTHQUAKE,
            },
            },
            {
#line 8373
            .species = SPECIES_BASCULIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8373
            .heldItem = ITEM_CHOICE_BAND,
#line 8376
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8375
            .ability = ABILITY_ADAPTABILITY,
#line 8374
            .lvl = 55,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 8377
                MOVE_WAVE_CRASH,
                MOVE_AQUA_JET,
                MOVE_HEAD_SMASH,
                MOVE_CRUNCH,
            },
            },
        },
    },
#line 8392
#line 8394
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_D] =
    {
#line 8393
        .trainerName = _("Tom"),
#line 8395
        .trainerClass = TRAINER_CLASS_DRAGON_TAMER,
#line 8396
        .trainerPic = TRAINER_PIC_DRAGON_TAMER,
        .encounterMusic_gender =
#line 8398
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8399
        .doubleBattle = FALSE,
#line 8400
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8402
            .species = SPECIES_SLIGGOO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8405
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8404
            .ability = ABILITY_GOOEY,
#line 8403
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8407
            .species = SPECIES_NOIVERN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8410
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8409
            .ability = ABILITY_INFILTRATOR,
#line 8408
            .lvl = 56,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8412
#line 8414
    [DIFFICULTY_NORMAL][TRAINER_VICTORY_ROAD_D] =
    {
#line 8413
        .trainerName = _("Tom"),
#line 8415
        .trainerClass = TRAINER_CLASS_DRAGON_TAMER,
#line 8416
        .trainerPic = TRAINER_PIC_DRAGON_TAMER,
        .encounterMusic_gender =
#line 8418
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8419
        .doubleBattle = FALSE,
#line 8420
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8422
            .species = SPECIES_SLIGGOO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8425
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8424
            .ability = ABILITY_GOOEY,
#line 8423
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8427
            .species = SPECIES_NOIVERN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8430
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8429
            .ability = ABILITY_INFILTRATOR,
#line 8428
            .lvl = 56,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8443
#line 8445
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_E] =
    {
#line 8444
        .trainerName = _("Anaya"),
#line 8446
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 8447
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 8449
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8450
        .doubleBattle = FALSE,
#line 8451
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8453
            .species = SPECIES_DRAGALGE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8455
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8454
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8457
            .species = SPECIES_ALOMOMOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8459
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8458
            .lvl = 56,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8461
#line 8463
    [DIFFICULTY_NORMAL][TRAINER_VICTORY_ROAD_E] =
    {
#line 8462
        .trainerName = _("Anaya"),
#line 8464
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 8465
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 8467
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8468
        .doubleBattle = FALSE,
#line 8469
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8471
            .species = SPECIES_DRAGALGE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8473
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8472
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8475
            .species = SPECIES_ALOMOMOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8477
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8476
            .lvl = 56,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8492
#line 8494
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_F] =
    {
#line 8493
        .trainerName = _("Toctay"),
#line 8495
        .trainerClass = TRAINER_CLASS_HIKER,
#line 8496
        .trainerPic = TRAINER_PIC_HIKER,
        .encounterMusic_gender =
#line 8498
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8499
        .doubleBattle = FALSE,
#line 8500
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 8502
            .species = SPECIES_GLIMMORA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8504
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8503
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8506
            .species = SPECIES_GOLEM_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8508
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8507
            .lvl = 55,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8510
            .species = SPECIES_DUGTRIO_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8512
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8511
            .lvl = 57,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8514
#line 8516
    [DIFFICULTY_NORMAL][TRAINER_VICTORY_ROAD_F] =
    {
#line 8515
        .trainerName = _("Toctay"),
#line 8517
        .trainerClass = TRAINER_CLASS_HIKER,
#line 8518
        .trainerPic = TRAINER_PIC_HIKER,
        .encounterMusic_gender =
#line 8520
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8521
        .doubleBattle = FALSE,
#line 8522
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 8524
            .species = SPECIES_GLIMMORA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8526
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8525
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8528
            .species = SPECIES_GOLEM_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8530
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8529
            .lvl = 55,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8532
            .species = SPECIES_DUGTRIO_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8534
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8533
            .lvl = 57,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8548
#line 8550
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_G] =
    {
#line 8549
        .trainerName = _("Yuna"),
#line 8551
        .trainerClass = TRAINER_CLASS_PKMN_BREEDER,
#line 8552
        .trainerPic = TRAINER_PIC_POKEMON_BREEDER_F,
        .encounterMusic_gender =
#line 8553
F_TRAINER_FEMALE | 
#line 8554
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8555
        .doubleBattle = FALSE,
#line 8556
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 8558
            .species = SPECIES_BRAVIARY_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8560
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8559
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8562
            .species = SPECIES_BOMBIRDIER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8564
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8563
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8566
            .species = SPECIES_SKARMORY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8568
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8567
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8570
            .species = SPECIES_TALONFLAME,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8572
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8571
            .lvl = 56,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8574
#line 8576
    [DIFFICULTY_NORMAL][TRAINER_VICTORY_ROAD_G] =
    {
#line 8575
        .trainerName = _("Yuna"),
#line 8577
        .trainerClass = TRAINER_CLASS_PKMN_BREEDER,
#line 8578
        .trainerPic = TRAINER_PIC_POKEMON_BREEDER_F,
        .encounterMusic_gender =
#line 8579
F_TRAINER_FEMALE | 
#line 8580
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8581
        .doubleBattle = FALSE,
#line 8582
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 8584
            .species = SPECIES_BRAVIARY_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8586
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8585
            .lvl = 52,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8588
            .species = SPECIES_BOMBIRDIER,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8590
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8589
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8592
            .species = SPECIES_SKARMORY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8594
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8593
            .lvl = 53,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8596
            .species = SPECIES_TALONFLAME,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8598
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8597
            .lvl = 56,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8613
#line 8615
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_H] =
    {
#line 8614
        .trainerName = _("Sai"),
#line 8616
        .trainerClass = TRAINER_CLASS_BACKPACKER,
#line 8617
        .trainerPic = TRAINER_PIC_BACKPACKER,
        .encounterMusic_gender =
#line 8619
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8620
        .doubleBattle = FALSE,
#line 8621
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 8623
            .species = SPECIES_FURRET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8625
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8624
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8627
            .species = SPECIES_FORRETRESS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8629
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8628
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8631
            .species = SPECIES_LYCANROC_MIDNIGHT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8633
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8632
            .lvl = 55,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8635
#line 8637
    [DIFFICULTY_NORMAL][TRAINER_VICTORY_ROAD_H] =
    {
#line 8636
        .trainerName = _("Sai"),
#line 8638
        .trainerClass = TRAINER_CLASS_BACKPACKER,
#line 8639
        .trainerPic = TRAINER_PIC_BACKPACKER,
        .encounterMusic_gender =
#line 8641
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8642
        .doubleBattle = FALSE,
#line 8643
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_FORCE_SETUP_FIRST_TURN,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 8645
            .species = SPECIES_FURRET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8645
            .heldItem = ITEM_SILK_SCARF,
#line 8647
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8646
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 8648
                MOVE_TIDY_UP,
                MOVE_LAST_RESORT,
            },
            },
            {
#line 8651
            .species = SPECIES_FORRETRESS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8653
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8652
            .lvl = 54,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8655
            .species = SPECIES_LYCANROC_MIDNIGHT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8657
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8656
            .lvl = 55,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8673
#line 8675
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_I] =
    {
#line 8674
        .trainerName = _("Kirk"),
#line 8676
        .trainerClass = TRAINER_CLASS_RICH_BOY,
#line 8677
        .trainerPic = TRAINER_PIC_RICH_BOY,
        .encounterMusic_gender =
#line 8679
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8680
        .doubleBattle = FALSE,
#line 8681
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 8683
            .species = SPECIES_CHARIZARD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8683
            .heldItem = ITEM_CHARIZARDITE_X,
#line 8686
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8684
            .lvl = 58,
            .nature = NATURE_HARDY,
#line 8685
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8688
#line 8690
    [DIFFICULTY_NORMAL][TRAINER_VICTORY_ROAD_I] =
    {
#line 8689
        .trainerName = _("Kirk"),
#line 8691
        .trainerClass = TRAINER_CLASS_RICH_BOY,
#line 8692
        .trainerPic = TRAINER_PIC_RICH_BOY,
        .encounterMusic_gender =
#line 8694
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8695
        .doubleBattle = FALSE,
#line 8696
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 8698
            .species = SPECIES_CHARIZARD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8698
            .heldItem = ITEM_CHARIZARDITE_X,
#line 8701
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8699
            .lvl = 58,
            .nature = NATURE_HARDY,
#line 8700
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8714
#line 8716
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_J] =
    {
#line 8715
        .trainerName = _("Pia"),
#line 8717
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 8718
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 8720
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8721
        .doubleBattle = FALSE,
#line 8722
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 8724
            .species = SPECIES_MASQUERAIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8726
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8725
            .lvl = 56,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8728
            .species = SPECIES_FROSMOTH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8730
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8729
            .lvl = 57,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8732
            .species = SPECIES_GOODRA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8734
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8733
            .lvl = 57,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8736
#line 8738
    [DIFFICULTY_NORMAL][TRAINER_VICTORY_ROAD_J] =
    {
#line 8737
        .trainerName = _("Pia"),
#line 8739
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 8740
        .trainerPic = TRAINER_PIC_COOLTRAINER_F,
        .encounterMusic_gender =
#line 8742
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8743
        .doubleBattle = FALSE,
#line 8744
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 8746
            .species = SPECIES_MASQUERAIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8748
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8747
            .lvl = 56,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8750
            .species = SPECIES_FROSMOTH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8752
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8751
            .lvl = 57,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8754
            .species = SPECIES_GOODRA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8756
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8755
            .lvl = 57,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8769
#line 8771
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_K] =
    {
#line 8770
        .trainerName = _("Grunt"),
#line 8772
        .trainerClass = TRAINER_CLASS_TEAM_AQUA,
#line 8773
        .trainerPic = TRAINER_PIC_AQUA_GRUNT_F,
        .encounterMusic_gender =
#line 8774
F_TRAINER_FEMALE | 
#line 8775
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 8776
        .doubleBattle = FALSE,
#line 8777
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8779
            .species = SPECIES_POOCHYENA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8781
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 8780
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8783
            .species = SPECIES_ZUBAT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8785
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 8784
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8798
#line 8800
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_L] =
    {
#line 8799
        .trainerName = _("Grunt"),
#line 8801
        .trainerClass = TRAINER_CLASS_TEAM_AQUA,
#line 8802
        .trainerPic = TRAINER_PIC_AQUA_GRUNT_M,
        .encounterMusic_gender =
#line 8804
            TRAINER_ENCOUNTER_MUSIC_AQUA,
#line 8805
        .doubleBattle = FALSE,
#line 8806
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 8808
            .species = SPECIES_CARVANHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8810
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 8809
            .lvl = 32,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8823
#line 8825
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_M] =
    {
#line 8824
        .trainerName = _("SHAWN"),
#line 8826
        .trainerClass = TRAINER_CLASS_GUITARIST,
#line 8827
        .trainerPic = TRAINER_PIC_GUITARIST,
        .encounterMusic_gender =
#line 8829
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8830
        .doubleBattle = FALSE,
#line 8831
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8833
            .species = SPECIES_VOLTORB,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8835
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 8834
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8837
            .species = SPECIES_MAGNEMITE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8839
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 8838
            .lvl = 17,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8852
#line 8854
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_N] =
    {
#line 8853
        .trainerName = _("FERNANDO"),
#line 8855
        .trainerClass = TRAINER_CLASS_GUITARIST,
#line 8856
        .trainerPic = TRAINER_PIC_GUITARIST,
        .encounterMusic_gender =
#line 8858
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8859
        .doubleBattle = FALSE,
#line 8860
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8862
            .species = SPECIES_ELECTRIKE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8864
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 8863
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8866
            .species = SPECIES_LOUDRED,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8868
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 8867
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8881
#line 8883
    [DIFFICULTY_EASY][TRAINER_VICTORY_ROAD_O] =
    {
#line 8882
        .trainerName = _("DALTON"),
#line 8884
        .trainerClass = TRAINER_CLASS_GUITARIST,
#line 8885
        .trainerPic = TRAINER_PIC_GUITARIST,
        .encounterMusic_gender =
#line 8887
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 8888
        .doubleBattle = FALSE,
#line 8889
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 8891
            .species = SPECIES_MAGNEMITE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8893
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 8892
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8895
            .species = SPECIES_WHISMUR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8897
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 8896
            .lvl = 15,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8910
#line 8912
    [DIFFICULTY_EASY][TRAINER_CHAMPIONSHIP_A] =
    {
#line 8911
        .trainerName = _("Chara"),
#line 8913
        .trainerClass = TRAINER_CLASS_CONTENDER,
#line 8914
        .trainerPic = TRAINER_PIC_COOL_GIRL,
        .encounterMusic_gender =
#line 8915
F_TRAINER_FEMALE | 
#line 8916
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 8917
        .doubleBattle = FALSE,
#line 8918
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_ACE_POKEMON,
#line 8919
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 8921
            .species = SPECIES_URSALUNA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8923
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8922
            .lvl = 57,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8925
            .species = SPECIES_TYPHLOSION_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8927
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8926
            .lvl = 58,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8929
            .species = SPECIES_FORRETRESS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8931
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8930
            .lvl = 58,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8933
            .species = SPECIES_BARRASKEWDA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8935
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8934
            .lvl = 59,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8937
            .species = SPECIES_ALTARIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8937
            .heldItem = ITEM_ALTARIANITE,
#line 8939
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8938
            .lvl = 61,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8941
#line 8943
    [DIFFICULTY_NORMAL][TRAINER_CHAMPIONSHIP_A] =
    {
#line 8942
        .trainerName = _("Chara"),
#line 8944
        .trainerClass = TRAINER_CLASS_CONTENDER,
#line 8945
        .trainerPic = TRAINER_PIC_COOL_GIRL,
        .encounterMusic_gender =
#line 8946
F_TRAINER_FEMALE | 
#line 8947
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 8948
        .doubleBattle = FALSE,
#line 8949
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_FORCE_SETUP_FIRST_TURN | AI_FLAG_ACE_POKEMON,
#line 8950
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 8952
            .species = SPECIES_MEGANIUM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8952
            .heldItem = ITEM_HEAT_ROCK,
#line 8954
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8953
            .lvl = 57,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 8955
                MOVE_SUNNY_DAY,
                MOVE_SOLAR_BEAM,
                MOVE_STOMPING_TANTRUM,
            },
            },
            {
#line 8959
            .species = SPECIES_URSALUNA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8959
            .heldItem = ITEM_FLAME_ORB,
#line 8962
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8960
            .ability = ABILITY_GUTS,
#line 8961
            .lvl = 58,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 8963
                MOVE_FACADE,
                MOVE_EARTHQUAKE,
            },
            },
            {
#line 8966
            .species = SPECIES_TYPHLOSION_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8966
            .heldItem = ITEM_CHOICE_SCARF,
#line 8968
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8967
            .lvl = 58,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 8969
                MOVE_OVERHEAT,
            },
            },
            {
#line 8971
            .species = SPECIES_FORRETRESS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8973
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8972
            .lvl = 59,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 8975
            .species = SPECIES_ALTARIA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 8975
            .heldItem = ITEM_ALTARIANITE,
#line 8977
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 8976
            .lvl = 61,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 8991
#line 8993
    [DIFFICULTY_EASY][TRAINER_CHAMPIONSHIP_B] =
    {
#line 8992
        .trainerName = _("Stanja"),
#line 8994
        .trainerClass = TRAINER_CLASS_CONTENDER,
#line 8995
        .trainerPic = TRAINER_PIC_BUG_MANIAC,
        .encounterMusic_gender =
#line 8997
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 8998
        .doubleBattle = FALSE,
#line 8999
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 9000
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 9002
            .species = SPECIES_GLIMMORA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9002
            .heldItem = ITEM_POWER_HERB,
#line 9004
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9003
            .lvl = 58,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9005
                MOVE_METEOR_BEAM,
                MOVE_SLUDGE_WAVE,
                MOVE_STEALTH_ROCK,
                MOVE_SOLAR_BEAM,
            },
            },
            {
#line 9010
            .species = SPECIES_SCOLIPEDE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9012
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9011
            .lvl = 59,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9014
            .species = SPECIES_AMOONGUSS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9014
            .heldItem = ITEM_ROCKY_HELMET,
#line 9016
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9015
            .lvl = 60,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9018
            .species = SPECIES_TOXAPEX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9020
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9019
            .lvl = 60,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9022
            .species = SPECIES_PINSIR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9022
            .heldItem = ITEM_PINSIRITE,
#line 9024
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9023
            .lvl = 61,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9025
                MOVE_X_SCISSOR,
                MOVE_SWORDS_DANCE,
                MOVE_QUICK_ATTACK,
                MOVE_DOUBLE_EDGE,
            },
            },
        },
    },
#line 9030
#line 9032
    [DIFFICULTY_NORMAL][TRAINER_CHAMPIONSHIP_B] =
    {
#line 9031
        .trainerName = _("Stanja"),
#line 9033
        .trainerClass = TRAINER_CLASS_CONTENDER,
#line 9034
        .trainerPic = TRAINER_PIC_BUG_MANIAC,
        .encounterMusic_gender =
#line 9036
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 9037
        .doubleBattle = FALSE,
#line 9038
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 9039
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 9041
            .species = SPECIES_GLIMMORA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9041
            .heldItem = ITEM_POWER_HERB,
#line 9043
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9042
            .lvl = 58,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9044
                MOVE_METEOR_BEAM,
                MOVE_SLUDGE_WAVE,
                MOVE_STEALTH_ROCK,
                MOVE_SOLAR_BEAM,
            },
            },
            {
#line 9049
            .species = SPECIES_SCOLIPEDE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9051
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9050
            .lvl = 59,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9053
            .species = SPECIES_AMOONGUSS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9053
            .heldItem = ITEM_ROCKY_HELMET,
#line 9055
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9054
            .lvl = 60,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9057
            .species = SPECIES_TOXAPEX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9057
            .heldItem = ITEM_LEFTOVERS,
#line 9059
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9058
            .lvl = 60,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9061
            .species = SPECIES_PINSIR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9061
            .heldItem = ITEM_PINSIRITE,
#line 9063
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9062
            .lvl = 61,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9064
                MOVE_X_SCISSOR,
                MOVE_SWORDS_DANCE,
                MOVE_QUICK_ATTACK,
                MOVE_DOUBLE_EDGE,
            },
            },
        },
    },
#line 9082
#line 9084
    [DIFFICULTY_EASY][TRAINER_CHAMPIONSHIP_C] =
    {
#line 9083
        .trainerName = _("Berger"),
#line 9085
        .trainerClass = TRAINER_CLASS_CONTENDER,
#line 9086
        .trainerPic = TRAINER_PIC_COOL_GUY,
        .encounterMusic_gender =
#line 9088
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 9089
        .doubleBattle = FALSE,
#line 9090
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON | AI_FLAG_FORCE_SETUP_FIRST_TURN,
#line 9091
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 9093
            .species = SPECIES_NINETALES_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9096
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9094
            .ability = ABILITY_SNOW_WARNING,
#line 9095
            .lvl = 60,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9097
                MOVE_AURORA_VEIL,
                MOVE_MOONBLAST,
                MOVE_BLIZZARD,
                MOVE_FREEZE_DRY,
            },
            },
            {
#line 9102
            .species = SPECIES_BAXCALIBUR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9105
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9103
            .ability = ABILITY_ICE_BODY,
#line 9104
            .lvl = 62,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9107
            .species = SPECIES_TINKATON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9109
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9108
            .lvl = 61,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9111
            .species = SPECIES_RAPIDASH_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9113
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9112
            .lvl = 60,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9115
            .species = SPECIES_AVALUGG_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9117
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9116
            .lvl = 62,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 9119
#line 9121
    [DIFFICULTY_NORMAL][TRAINER_CHAMPIONSHIP_C] =
    {
#line 9120
        .trainerName = _("Berger"),
#line 9122
        .trainerClass = TRAINER_CLASS_CONTENDER,
#line 9123
        .trainerPic = TRAINER_PIC_COOL_GUY,
        .encounterMusic_gender =
#line 9125
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 9126
        .doubleBattle = FALSE,
#line 9127
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON | AI_FLAG_FORCE_SETUP_FIRST_TURN,
#line 9128
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 9130
            .species = SPECIES_NINETALES_ALOLA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9130
            .heldItem = ITEM_ICY_ROCK,
#line 9133
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9131
            .ability = ABILITY_SNOW_WARNING,
#line 9132
            .lvl = 60,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9134
                MOVE_AURORA_VEIL,
                MOVE_MOONBLAST,
                MOVE_BLIZZARD,
                MOVE_FREEZE_DRY,
            },
            },
            {
#line 9139
            .species = SPECIES_BAXCALIBUR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9142
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9140
            .ability = ABILITY_ICE_BODY,
#line 9141
            .lvl = 62,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9144
            .species = SPECIES_TINKATON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9146
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9145
            .lvl = 61,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9148
            .species = SPECIES_RAPIDASH_GALAR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9150
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9149
            .lvl = 60,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9152
            .species = SPECIES_AVALUGG_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9154
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9153
            .lvl = 63,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 9166
#line 9168
    [DIFFICULTY_EASY][TRAINER_CHAMPIONSHIP_D] =
    {
#line 9167
        .trainerName = _("Gabrielle"),
#line 9169
        .trainerClass = TRAINER_CLASS_CONTENDER,
#line 9170
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 9171
F_TRAINER_FEMALE | 
#line 9172
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 9173
        .doubleBattle = FALSE,
#line 9174
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 9175
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 9177
            .species = SPECIES_CLAYDOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9179
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9178
            .lvl = 62,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9180
                MOVE_STEALTH_ROCK,
                MOVE_PSYCHIC,
                MOVE_SCORCHING_SANDS,
                MOVE_TOXIC,
            },
            },
            {
#line 9186
            .species = SPECIES_ZOROARK_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9186
            .heldItem = ITEM_LIFE_ORB,
#line 9188
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9187
            .lvl = 62,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9189
                MOVE_NASTY_PLOT,
                MOVE_SHADOW_BALL,
                MOVE_HYPER_VOICE,
                MOVE_FOCUS_BLAST,
            },
            },
            {
#line 9194
            .species = SPECIES_KOMMO_O,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9196
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9195
            .lvl = 61,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9197
                MOVE_CLANGOROUS_SOUL,
                MOVE_CLANGING_SCALES,
                MOVE_BOOMBURST,
                MOVE_EARTHQUAKE,
            },
            },
            {
#line 9202
            .species = SPECIES_MILOTIC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9202
            .heldItem = ITEM_SITRUS_BERRY,
#line 9205
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9204
            .ability = ABILITY_COMPETITIVE,
#line 9203
            .lvl = 61,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9206
                MOVE_CALM_MIND,
                MOVE_SCALD,
                MOVE_RECOVER,
                MOVE_CONFUSE_RAY,
            },
            },
            {
#line 9211
            .species = SPECIES_MAWILE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9211
            .heldItem = ITEM_MAWILITE,
#line 9213
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9212
            .lvl = 62,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9214
                MOVE_SWORDS_DANCE,
                MOVE_PLAY_ROUGH,
                MOVE_SUCKER_PUNCH,
                MOVE_BRICK_BREAK,
            },
            },
        },
    },
#line 9219
#line 9221
    [DIFFICULTY_NORMAL][TRAINER_CHAMPIONSHIP_D] =
    {
#line 9220
        .trainerName = _("Gabrielle"),
#line 9222
        .trainerClass = TRAINER_CLASS_CONTENDER,
#line 9223
        .trainerPic = TRAINER_PIC_SOMBER_GRUNT_F,
        .encounterMusic_gender =
#line 9224
F_TRAINER_FEMALE | 
#line 9225
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 9226
        .doubleBattle = FALSE,
#line 9227
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 9228
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 9230
            .species = SPECIES_CLAYDOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9230
            .heldItem = ITEM_LEFTOVERS,
#line 9232
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9231
            .lvl = 62,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9233
                MOVE_STEALTH_ROCK,
                MOVE_PSYCHIC,
                MOVE_SCORCHING_SANDS,
                MOVE_TOXIC,
            },
            },
            {
#line 9239
            .species = SPECIES_ZOROARK_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9239
            .heldItem = ITEM_LIFE_ORB,
#line 9241
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9240
            .lvl = 63,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9242
                MOVE_NASTY_PLOT,
                MOVE_SHADOW_BALL,
                MOVE_HYPER_VOICE,
                MOVE_FOCUS_BLAST,
            },
            },
            {
#line 9247
            .species = SPECIES_KOMMO_O,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9247
            .heldItem = ITEM_THROAT_SPRAY,
#line 9249
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9248
            .lvl = 63,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9250
                MOVE_CLANGOROUS_SOUL,
                MOVE_CLANGING_SCALES,
                MOVE_BOOMBURST,
                MOVE_EARTHQUAKE,
            },
            },
            {
#line 9255
            .species = SPECIES_MILOTIC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9255
            .heldItem = ITEM_SITRUS_BERRY,
#line 9258
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9257
            .ability = ABILITY_COMPETITIVE,
#line 9256
            .lvl = 62,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9259
                MOVE_CALM_MIND,
                MOVE_SCALD,
                MOVE_RECOVER,
                MOVE_CONFUSE_RAY,
            },
            },
            {
#line 9264
            .species = SPECIES_MAWILE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9264
            .heldItem = ITEM_MAWILITE,
#line 9266
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9265
            .lvl = 63,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9267
                MOVE_SWORDS_DANCE,
                MOVE_PLAY_ROUGH,
                MOVE_SUCKER_PUNCH,
                MOVE_BRICK_BREAK,
            },
            },
        },
    },
#line 9283
#line 9285
    [DIFFICULTY_EASY][TRAINER_CHAMPIONSHIP_E] =
    {
#line 9284
        .trainerName = _("Kohla"),
#line 9286
        .trainerClass = TRAINER_CLASS_KOHLA_FINAL,
#line 9287
        .trainerPic = TRAINER_PIC_WALLY,
        .encounterMusic_gender =
#line 9289
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 9290
        .doubleBattle = FALSE,
#line 9291
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 9292
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 9294
            .species = SPECIES_SAMUROTT_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9294
            .heldItem = ITEM_LEFTOVERS,
#line 9297
            .ev = TRAINER_PARTY_EVS(252, 0, 116, 0, 0, 140),
#line 9298
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9295
            .ability = ABILITY_SHARPNESS,
#line 9296
            .lvl = 62,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9299
                MOVE_FLIP_TURN,
                MOVE_AQUA_JET,
                MOVE_SACRED_SWORD,
            },
            },
            {
#line 9303
            .species = SPECIES_KLEAVOR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9303
            .heldItem = ITEM_FOCUS_SASH,
#line 9306
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9304
            .ability = ABILITY_SHARPNESS,
#line 9305
            .lvl = 62,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9307
                MOVE_STONE_AXE,
                MOVE_X_SCISSOR,
                MOVE_TRAILBLAZE,
            },
            },
            {
#line 9311
            .species = SPECIES_TOGEKISS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9311
            .heldItem = ITEM_LEFTOVERS,
#line 9314
            .ev = TRAINER_PARTY_EVS(116, 0, 0, 0, 0, 0),
#line 9315
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9312
            .ability = ABILITY_SERENE_GRACE,
#line 9313
            .lvl = 63,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9316
                MOVE_ANCIENT_POWER,
                MOVE_AIR_SLASH,
                MOVE_NASTY_PLOT,
                MOVE_ROOST,
            },
            },
            {
#line 9321
            .species = SPECIES_AEGISLASH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9321
            .heldItem = ITEM_AIR_BALLOON,
#line 9323
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9322
            .lvl = 63,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9324
                MOVE_KINGS_SHIELD,
                MOVE_SHADOW_BALL,
                MOVE_SHADOW_SNEAK,
                MOVE_FLASH_CANNON,
            },
            },
            {
#line 9329
            .species = SPECIES_GALLADE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9329
            .heldItem = ITEM_GALLADITE,
#line 9331
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9330
            .lvl = 64,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9332
                MOVE_DRAIN_PUNCH,
                MOVE_ZEN_HEADBUTT,
                MOVE_SHADOW_SNEAK,
                MOVE_FIRE_PUNCH,
            },
            },
            {
#line 9337
            .species = SPECIES_CERULEDGE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9337
            .heldItem = ITEM_LIFE_ORB,
#line 9340
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9338
            .ability = ABILITY_WEAK_ARMOR,
#line 9339
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9341
                MOVE_BITTER_BLADE,
                MOVE_SWORDS_DANCE,
                MOVE_SHADOW_SNEAK,
                MOVE_CLOSE_COMBAT,
            },
            },
        },
    },
#line 9346
#line 9348
    [DIFFICULTY_NORMAL][TRAINER_CHAMPIONSHIP_E] =
    {
#line 9347
        .trainerName = _("Kohla"),
#line 9349
        .trainerClass = TRAINER_CLASS_KOHLA_FINAL,
#line 9350
        .trainerPic = TRAINER_PIC_WALLY,
        .encounterMusic_gender =
#line 9352
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 9353
        .doubleBattle = FALSE,
#line 9354
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 9355
        .mugshotColor = MUGSHOT_COLOR_GREEN,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 9357
            .species = SPECIES_SAMUROTT_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9357
            .heldItem = ITEM_LEFTOVERS,
#line 9360
            .ev = TRAINER_PARTY_EVS(252, 0, 116, 0, 0, 140),
#line 9361
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9358
            .ability = ABILITY_SHARPNESS,
#line 9359
            .lvl = 62,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9362
                MOVE_FLIP_TURN,
                MOVE_CEASELESS_EDGE,
                MOVE_AQUA_JET,
                MOVE_SACRED_SWORD,
            },
            },
            {
#line 9367
            .species = SPECIES_KLEAVOR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9367
            .heldItem = ITEM_FOCUS_SASH,
#line 9370
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9368
            .ability = ABILITY_SHARPNESS,
#line 9369
            .lvl = 62,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9371
                MOVE_STONE_AXE,
                MOVE_X_SCISSOR,
                MOVE_TRAILBLAZE,
            },
            },
            {
#line 9375
            .species = SPECIES_TOGEKISS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9375
            .heldItem = ITEM_LEFTOVERS,
#line 9378
            .ev = TRAINER_PARTY_EVS(252, 0, 116, 0, 0, 140),
#line 9379
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9376
            .ability = ABILITY_SERENE_GRACE,
#line 9377
            .lvl = 63,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9380
                MOVE_THUNDER_WAVE,
                MOVE_AIR_SLASH,
                MOVE_NASTY_PLOT,
                MOVE_ROOST,
            },
            },
            {
#line 9385
            .species = SPECIES_AEGISLASH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9385
            .heldItem = ITEM_AIR_BALLOON,
#line 9387
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9386
            .lvl = 63,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9388
                MOVE_KINGS_SHIELD,
                MOVE_SHADOW_BALL,
                MOVE_SHADOW_SNEAK,
                MOVE_FLASH_CANNON,
            },
            },
            {
#line 9393
            .species = SPECIES_GALLADE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9393
            .heldItem = ITEM_GALLADITE,
#line 9395
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9394
            .lvl = 64,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9396
                MOVE_DRAIN_PUNCH,
                MOVE_ZEN_HEADBUTT,
                MOVE_SHADOW_SNEAK,
                MOVE_FIRE_PUNCH,
            },
            },
            {
#line 9401
            .species = SPECIES_CERULEDGE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9401
            .heldItem = ITEM_LIFE_ORB,
#line 9404
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9402
            .ability = ABILITY_WEAK_ARMOR,
#line 9403
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9405
                MOVE_BITTER_BLADE,
                MOVE_SWORDS_DANCE,
                MOVE_SHADOW_SNEAK,
                MOVE_CLOSE_COMBAT,
            },
            },
        },
    },
#line 9428
#line 9430
    [DIFFICULTY_EASY][TRAINER_VICTORYCAPE_A] =
    {
#line 9429
        .trainerName = _("Shiina"),
#line 9431
        .trainerClass = TRAINER_CLASS_AROMA_LADY,
#line 9432
        .trainerPic = TRAINER_PIC_AROMA_LADY,
        .encounterMusic_gender =
#line 9433
F_TRAINER_FEMALE | 
#line 9434
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 9435
        .doubleBattle = FALSE,
#line 9436
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 9438
            .species = SPECIES_SHIINOTIC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9440
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9439
            .lvl = 57,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9441
            .species = SPECIES_FORRETRESS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9443
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9442
            .lvl = 60,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 9444
#line 9446
    [DIFFICULTY_NORMAL][TRAINER_VICTORYCAPE_A] =
    {
#line 9445
        .trainerName = _("Shiina"),
#line 9447
        .trainerClass = TRAINER_CLASS_AROMA_LADY,
#line 9448
        .trainerPic = TRAINER_PIC_AROMA_LADY,
        .encounterMusic_gender =
#line 9449
F_TRAINER_FEMALE | 
#line 9450
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 9451
        .doubleBattle = FALSE,
#line 9452
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 9454
            .species = SPECIES_SHIINOTIC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9456
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9455
            .lvl = 57,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9457
            .species = SPECIES_FORRETRESS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9459
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9458
            .lvl = 60,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 9469
#line 9471
    [DIFFICULTY_EASY][TRAINER_VICTORYCAPE_B] =
    {
#line 9470
        .trainerName = _("Axel"),
#line 9472
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 9473
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 9475
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 9476
        .doubleBattle = FALSE,
#line 9477
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 9479
            .species = SPECIES_CETITAN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9481
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9480
            .lvl = 58,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9482
            .species = SPECIES_CHANDELURE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9484
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9483
            .lvl = 60,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 9485
#line 9487
    [DIFFICULTY_NORMAL][TRAINER_VICTORYCAPE_B] =
    {
#line 9486
        .trainerName = _("Axel"),
#line 9488
        .trainerClass = TRAINER_CLASS_COOLTRAINER,
#line 9489
        .trainerPic = TRAINER_PIC_COOLTRAINER_M,
        .encounterMusic_gender =
#line 9491
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 9492
        .doubleBattle = FALSE,
#line 9493
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 9495
            .species = SPECIES_CETITAN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9497
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9496
            .lvl = 58,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 9498
            .species = SPECIES_CHANDELURE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9500
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9499
            .lvl = 60,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 9506
#line 9508
    [DIFFICULTY_EASY][TRAINER_PLAYER_SENTRY] =
    {
#line 9507
        .trainerName = _("Sentry"),
#line 9509
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 9510
        .trainerPic = TRAINER_PIC_GUBUKING,
        .encounterMusic_gender =
#line 9512
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 9514
        .items = { ITEM_FULL_RESTORE },
#line 9513
        .doubleBattle = FALSE,
#line 9515
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION,
#line 9516
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 9518
            .species = SPECIES_TYPHLOSION_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9521
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9520
            .ability = ABILITY_FRISK,
#line 9519
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9522
                MOVE_FLAMETHROWER,
                MOVE_SHADOW_BALL,
                MOVE_INFERNAL_PARADE,
                MOVE_SWIFT,
            },
            },
            {
#line 9527
            .species = SPECIES_AGGRON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9527
            .heldItem = ITEM_AGGRONITE,
#line 9531
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9529
            .ability = ABILITY_ROCK_HEAD,
#line 9528
            .lvl = 69,
#line 9530
            .nature = NATURE_RELAXED,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9532
                MOVE_IRON_HEAD,
                MOVE_DRAGON_CLAW,
                MOVE_EARTHQUAKE,
                MOVE_STRENGTH,
            },
            },
            {
#line 9537
            .species = SPECIES_DRAGAPULT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9541
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9539
            .ability = ABILITY_CURSED_BODY,
#line 9538
            .lvl = 66,
#line 9540
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9542
                MOVE_DRAGON_CLAW,
                MOVE_BITE,
                MOVE_DRAGON_DARTS,
                MOVE_PHANTOM_FORCE,
            },
            },
            {
#line 9547
            .species = SPECIES_OBSTAGOON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9551
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9549
            .ability = ABILITY_DEFIANT,
#line 9548
            .lvl = 66,
#line 9550
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9552
                MOVE_HEADBUTT,
                MOVE_PIN_MISSILE,
                MOVE_CROSS_CHOP,
                MOVE_NIGHT_SLASH,
            },
            },
            {
#line 9557
            .species = SPECIES_SEISMITOAD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9561
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9559
            .ability = ABILITY_WATER_ABSORB,
#line 9558
            .lvl = 66,
#line 9560
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9562
                MOVE_DIVE,
                MOVE_AQUA_RING,
                MOVE_MUDDY_WATER,
                MOVE_DRAIN_PUNCH,
            },
            },
            {
#line 9567
            .species = SPECIES_SINISTCHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9571
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9569
            .ability = ABILITY_HEATPROOF,
#line 9568
            .lvl = 66,
#line 9570
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9572
                MOVE_MATCHA_GOTCHA,
                MOVE_STRENGTH_SAP,
                MOVE_SHADOW_BALL,
                MOVE_FOUL_PLAY,
            },
            },
        },
    },
#line 9578
#line 9580
    [DIFFICULTY_NORMAL][TRAINER_PLAYER_SENTRY] =
    {
#line 9579
        .trainerName = _("Sentry"),
#line 9581
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 9582
        .trainerPic = TRAINER_PIC_GUBUKING,
        .encounterMusic_gender =
#line 9584
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 9586
        .items = { ITEM_FULL_RESTORE },
#line 9585
        .doubleBattle = FALSE,
#line 9587
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION,
#line 9588
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 9590
            .species = SPECIES_TYPHLOSION_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9593
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9592
            .ability = ABILITY_FRISK,
#line 9591
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9594
                MOVE_FLAMETHROWER,
                MOVE_SHADOW_BALL,
                MOVE_INFERNAL_PARADE,
                MOVE_SWIFT,
            },
            },
            {
#line 9599
            .species = SPECIES_AGGRON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9599
            .heldItem = ITEM_AGGRONITE,
#line 9603
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9601
            .ability = ABILITY_ROCK_HEAD,
#line 9600
            .lvl = 69,
#line 9602
            .nature = NATURE_RELAXED,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9604
                MOVE_IRON_HEAD,
                MOVE_DRAGON_CLAW,
                MOVE_EARTHQUAKE,
                MOVE_STRENGTH,
            },
            },
            {
#line 9609
            .species = SPECIES_DRAGAPULT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9613
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9611
            .ability = ABILITY_CURSED_BODY,
#line 9610
            .lvl = 66,
#line 9612
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9614
                MOVE_DRAGON_CLAW,
                MOVE_BITE,
                MOVE_DRAGON_DARTS,
                MOVE_PHANTOM_FORCE,
            },
            },
            {
#line 9619
            .species = SPECIES_OBSTAGOON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9623
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9621
            .ability = ABILITY_DEFIANT,
#line 9620
            .lvl = 66,
#line 9622
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9624
                MOVE_HEADBUTT,
                MOVE_PIN_MISSILE,
                MOVE_CROSS_CHOP,
                MOVE_NIGHT_SLASH,
            },
            },
            {
#line 9629
            .species = SPECIES_SEISMITOAD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9633
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9631
            .ability = ABILITY_WATER_ABSORB,
#line 9630
            .lvl = 66,
#line 9632
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9634
                MOVE_DIVE,
                MOVE_AQUA_RING,
                MOVE_MUDDY_WATER,
                MOVE_DRAIN_PUNCH,
            },
            },
            {
#line 9639
            .species = SPECIES_SINISTCHA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9643
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9641
            .ability = ABILITY_HEATPROOF,
#line 9640
            .lvl = 66,
#line 9642
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9644
                MOVE_MATCHA_GOTCHA,
                MOVE_STRENGTH_SAP,
                MOVE_SHADOW_BALL,
                MOVE_FOUL_PLAY,
            },
            },
        },
    },
#line 9660
#line 9662
    [DIFFICULTY_EASY][TRAINER_PLAYER_EDEN] =
    {
#line 9661
        .trainerName = _("Eden"),
#line 9663
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 9664
        .trainerPic = TRAINER_PIC_GUBUKING,
        .encounterMusic_gender =
#line 9666
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 9668
        .items = { ITEM_FULL_RESTORE },
#line 9667
        .doubleBattle = FALSE,
#line 9669
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION,
#line 9670
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 9672
            .species = SPECIES_OBSTAGOON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9672
            .heldItem = ITEM_ASSAULT_VEST,
#line 9675
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9674
            .ability = ABILITY_DEFIANT,
#line 9673
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9676
                MOVE_NIGHT_SLASH,
                MOVE_RETURN,
                MOVE_PIN_MISSILE,
                MOVE_LICK,
            },
            },
            {
#line 9681
            .species = SPECIES_SKARMORY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9681
            .heldItem = ITEM_MUSCLE_BAND,
#line 9684
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9683
            .ability = ABILITY_KEEN_EYE,
#line 9682
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9685
                MOVE_BRAVE_BIRD,
                MOVE_SPIKES,
                MOVE_SLASH,
                MOVE_STEEL_WING,
            },
            },
            {
#line 9690
            .species = SPECIES_SCREAM_TAIL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9690
            .heldItem = ITEM_FAIRY_FEATHER,
#line 9693
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9692
            .ability = ABILITY_PROTOSYNTHESIS,
#line 9691
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9694
                MOVE_PLAY_ROUGH,
                MOVE_PSYCHIC_FANGS,
                MOVE_CRUNCH,
                MOVE_NOBLE_ROAR,
            },
            },
            {
#line 9699
            .species = SPECIES_MILOTIC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9699
            .heldItem = ITEM_LEFTOVERS,
#line 9702
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9701
            .ability = ABILITY_COMPETITIVE,
#line 9700
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9703
                MOVE_SURF,
                MOVE_RECOVER,
                MOVE_ICE_BEAM,
                MOVE_TOXIC,
            },
            },
            {
#line 9708
            .species = SPECIES_MEDICHAM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9708
            .heldItem = ITEM_MEDICHAMITE,
#line 9711
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9710
            .ability = ABILITY_PURE_POWER,
#line 9709
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9712
                MOVE_ZEN_HEADBUTT,
                MOVE_FIRE_PUNCH,
                MOVE_AXE_KICK,
                MOVE_ICE_PUNCH,
            },
            },
            {
#line 9717
            .species = SPECIES_POLTEAGEIST,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9717
            .heldItem = ITEM_BIG_ROOT,
#line 9720
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9719
            .ability = ABILITY_WEAK_ARMOR,
#line 9718
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9721
                MOVE_SUCKER_PUNCH,
                MOVE_SHADOW_BALL,
                MOVE_STRENGTH_SAP,
                MOVE_GIGA_DRAIN,
            },
            },
        },
    },
#line 9727
#line 9729
    [DIFFICULTY_NORMAL][TRAINER_PLAYER_EDEN] =
    {
#line 9728
        .trainerName = _("Eden"),
#line 9730
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 9731
        .trainerPic = TRAINER_PIC_GUBUKING,
        .encounterMusic_gender =
#line 9733
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 9735
        .items = { ITEM_FULL_RESTORE },
#line 9734
        .doubleBattle = FALSE,
#line 9736
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION,
#line 9737
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 9739
            .species = SPECIES_OBSTAGOON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9739
            .heldItem = ITEM_ASSAULT_VEST,
#line 9742
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9741
            .ability = ABILITY_DEFIANT,
#line 9740
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9743
                MOVE_NIGHT_SLASH,
                MOVE_RETURN,
                MOVE_PIN_MISSILE,
                MOVE_LICK,
            },
            },
            {
#line 9748
            .species = SPECIES_SKARMORY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9748
            .heldItem = ITEM_MUSCLE_BAND,
#line 9751
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9750
            .ability = ABILITY_KEEN_EYE,
#line 9749
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9752
                MOVE_BRAVE_BIRD,
                MOVE_SPIKES,
                MOVE_SLASH,
                MOVE_STEEL_WING,
            },
            },
            {
#line 9757
            .species = SPECIES_SCREAM_TAIL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9757
            .heldItem = ITEM_FAIRY_FEATHER,
#line 9760
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9759
            .ability = ABILITY_PROTOSYNTHESIS,
#line 9758
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9761
                MOVE_PLAY_ROUGH,
                MOVE_PSYCHIC_FANGS,
                MOVE_CRUNCH,
                MOVE_NOBLE_ROAR,
            },
            },
            {
#line 9766
            .species = SPECIES_MILOTIC,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9766
            .heldItem = ITEM_LEFTOVERS,
#line 9769
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9768
            .ability = ABILITY_COMPETITIVE,
#line 9767
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9770
                MOVE_SURF,
                MOVE_RECOVER,
                MOVE_ICE_BEAM,
                MOVE_TOXIC,
            },
            },
            {
#line 9775
            .species = SPECIES_MEDICHAM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9775
            .heldItem = ITEM_MEDICHAMITE,
#line 9778
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9777
            .ability = ABILITY_PURE_POWER,
#line 9776
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9779
                MOVE_ZEN_HEADBUTT,
                MOVE_FIRE_PUNCH,
                MOVE_AXE_KICK,
                MOVE_ICE_PUNCH,
            },
            },
            {
#line 9784
            .species = SPECIES_POLTEAGEIST,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9784
            .heldItem = ITEM_BIG_ROOT,
#line 9787
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9786
            .ability = ABILITY_WEAK_ARMOR,
#line 9785
            .lvl = 65,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9788
                MOVE_SUCKER_PUNCH,
                MOVE_SHADOW_BALL,
                MOVE_STRENGTH_SAP,
                MOVE_GIGA_DRAIN,
            },
            },
        },
    },
#line 9804
#line 9806
    [DIFFICULTY_EASY][TRAINER_PLAYER_GOZLIAK] =
    {
#line 9805
        .trainerName = _("Gozliak"),
#line 9807
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 9808
        .trainerPic = TRAINER_PIC_BRENDAN,
        .encounterMusic_gender =
#line 9810
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 9812
        .items = { ITEM_FULL_RESTORE },
#line 9811
        .doubleBattle = FALSE,
#line 9813
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 9814
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 9816
            .species = SPECIES_HYDRAPPLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9816
            .heldItem = ITEM_CLEAR_AMULET,
#line 9821
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9818
            .ability = ABILITY_SUPERSWEET_SYRUP,
#line 9817
            .lvl = 67,
#line 9820
            .nature = NATURE_JOLLY,
#line 9819
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9822
                MOVE_GIGA_DRAIN,
                MOVE_SYRUP_BOMB,
                MOVE_FICKLE_BEAM,
                MOVE_GROWTH,
            },
            },
            {
#line 9827
            .species = SPECIES_GALLADE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9832
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9829
            .ability = ABILITY_JUSTIFIED,
#line 9828
            .lvl = 67,
#line 9831
            .nature = NATURE_JOLLY,
#line 9830
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9833
                MOVE_LEAF_BLADE,
                MOVE_CLOSE_COMBAT,
                MOVE_NIGHT_SLASH,
                MOVE_PSYCHO_CUT,
            },
            },
            {
#line 9838
            .species = SPECIES_TINKATON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9838
            .heldItem = ITEM_CLEAR_AMULET,
#line 9843
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9840
            .ability = ABILITY_PICKPOCKET,
#line 9839
            .lvl = 64,
#line 9842
            .nature = NATURE_JOLLY,
#line 9841
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9844
                MOVE_FAKE_OUT,
                MOVE_GIGATON_HAMMER,
                MOVE_KNOCK_OFF,
                MOVE_PLAY_ROUGH,
            },
            },
            {
#line 9849
            .species = SPECIES_MAWILE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9849
            .heldItem = ITEM_MAWILITE,
#line 9853
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9851
            .ability = ABILITY_HYPER_CUTTER,
#line 9850
            .lvl = 67,
#line 9852
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9854
                MOVE_PLAY_ROUGH,
                MOVE_IRON_DEFENSE,
                MOVE_SUCKER_PUNCH,
                MOVE_IRON_HEAD,
            },
            },
            {
#line 9859
            .species = SPECIES_CORVIKNIGHT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9859
            .heldItem = ITEM_CLEAR_AMULET,
#line 9864
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9861
            .ability = ABILITY_MIRROR_ARMOR,
#line 9860
            .lvl = 67,
#line 9863
            .nature = NATURE_JOLLY,
#line 9862
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9865
                MOVE_BRAVE_BIRD,
                MOVE_POWER_TRIP,
                MOVE_STEEL_WING,
                MOVE_TAUNT,
            },
            },
            {
#line 9870
            .species = SPECIES_OVERQWIL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9874
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9872
            .ability = ABILITY_POISON_POINT,
#line 9871
            .lvl = 67,
            .nature = NATURE_HARDY,
#line 9873
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9875
                MOVE_SURF,
                MOVE_BARB_BARRAGE,
                MOVE_CRUNCH,
                MOVE_TOXIC,
            },
            },
        },
    },
#line 9880
#line 9882
    [DIFFICULTY_NORMAL][TRAINER_PLAYER_GOZLIAK] =
    {
#line 9881
        .trainerName = _("Gozliak"),
#line 9883
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 9884
        .trainerPic = TRAINER_PIC_BRENDAN,
        .encounterMusic_gender =
#line 9886
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 9888
        .items = { ITEM_FULL_RESTORE },
#line 9887
        .doubleBattle = FALSE,
#line 9889
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 9890
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 9892
            .species = SPECIES_HYDRAPPLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9892
            .heldItem = ITEM_CLEAR_AMULET,
#line 9897
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9894
            .ability = ABILITY_SUPERSWEET_SYRUP,
#line 9893
            .lvl = 67,
#line 9896
            .nature = NATURE_JOLLY,
#line 9895
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9898
                MOVE_GIGA_DRAIN,
                MOVE_SYRUP_BOMB,
                MOVE_FICKLE_BEAM,
                MOVE_GROWTH,
            },
            },
            {
#line 9903
            .species = SPECIES_GALLADE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9908
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9905
            .ability = ABILITY_JUSTIFIED,
#line 9904
            .lvl = 67,
#line 9907
            .nature = NATURE_JOLLY,
#line 9906
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9909
                MOVE_LEAF_BLADE,
                MOVE_CLOSE_COMBAT,
                MOVE_NIGHT_SLASH,
                MOVE_PSYCHO_CUT,
            },
            },
            {
#line 9914
            .species = SPECIES_TINKATON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9914
            .heldItem = ITEM_CLEAR_AMULET,
#line 9919
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9916
            .ability = ABILITY_PICKPOCKET,
#line 9915
            .lvl = 64,
#line 9918
            .nature = NATURE_JOLLY,
#line 9917
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9920
                MOVE_FAKE_OUT,
                MOVE_GIGATON_HAMMER,
                MOVE_KNOCK_OFF,
                MOVE_PLAY_ROUGH,
            },
            },
            {
#line 9925
            .species = SPECIES_MAWILE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9925
            .heldItem = ITEM_MAWILITE,
#line 9929
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9927
            .ability = ABILITY_HYPER_CUTTER,
#line 9926
            .lvl = 67,
#line 9928
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9930
                MOVE_PLAY_ROUGH,
                MOVE_IRON_DEFENSE,
                MOVE_SUCKER_PUNCH,
                MOVE_IRON_HEAD,
            },
            },
            {
#line 9935
            .species = SPECIES_CORVIKNIGHT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9935
            .heldItem = ITEM_CLEAR_AMULET,
#line 9940
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9937
            .ability = ABILITY_MIRROR_ARMOR,
#line 9936
            .lvl = 67,
#line 9939
            .nature = NATURE_JOLLY,
#line 9938
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9941
                MOVE_BRAVE_BIRD,
                MOVE_POWER_TRIP,
                MOVE_STEEL_WING,
                MOVE_TAUNT,
            },
            },
            {
#line 9946
            .species = SPECIES_OVERQWIL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9950
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9948
            .ability = ABILITY_POISON_POINT,
#line 9947
            .lvl = 67,
            .nature = NATURE_HARDY,
#line 9949
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9951
                MOVE_SURF,
                MOVE_BARB_BARRAGE,
                MOVE_CRUNCH,
                MOVE_TOXIC,
            },
            },
        },
    },
#line 9968
#line 9970
    [DIFFICULTY_EASY][TRAINER_PLAYER_SHERRY] =
    {
#line 9969
        .trainerName = _("Sherry"),
#line 9971
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 9972
        .trainerPic = TRAINER_PIC_BRENDAN,
        .encounterMusic_gender =
#line 9974
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 9976
        .items = { ITEM_FULL_RESTORE },
#line 9975
        .doubleBattle = FALSE,
#line 9977
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 9978
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 9980
            .species = SPECIES_EXCADRILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9980
            .heldItem = ITEM_CLEAR_AMULET,
#line 9984
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9982
            .ability = ABILITY_SAND_FORCE,
#line 9981
            .lvl = 64,
#line 9983
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9985
                MOVE_STRENGTH,
                MOVE_ROCK_SLIDE,
                MOVE_EARTHQUAKE,
                MOVE_METAL_CLAW,
            },
            },
            {
#line 9990
            .species = SPECIES_MIMIKYU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 9990
            .heldItem = ITEM_LEFTOVERS,
#line 9994
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 9992
            .ability = ABILITY_DISGUISE,
#line 9991
            .lvl = 63,
#line 9993
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 9995
                MOVE_SHADOW_CLAW,
                MOVE_PLAY_ROUGH,
                MOVE_HONE_CLAWS,
                MOVE_WOOD_HAMMER,
            },
            },
            {
#line 10000
            .species = SPECIES_ROSERADE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10000
            .heldItem = ITEM_BIG_ROOT,
#line 10004
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10002
            .ability = ABILITY_NATURAL_CURE,
#line 10001
            .lvl = 63,
#line 10003
            .nature = NATURE_TIMID,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10005
                MOVE_GIGA_DRAIN,
                MOVE_GROWTH,
                MOVE_STUN_SPORE,
                MOVE_SLUDGE_BOMB,
            },
            },
            {
#line 10010
            .species = SPECIES_GOTHITELLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10010
            .heldItem = ITEM_PSYCHIC_GEM,
#line 10014
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10012
            .ability = ABILITY_FRISK,
#line 10011
            .lvl = 64,
#line 10013
            .nature = NATURE_TIMID,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10015
                MOVE_SHADOW_BALL,
                MOVE_PSYCHIC,
                MOVE_CALM_MIND,
                MOVE_THUNDERBOLT,
            },
            },
            {
#line 10020
            .species = SPECIES_AERODACTYL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10020
            .heldItem = ITEM_AERODACTYLITE,
#line 10024
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10022
            .ability = ABILITY_ROCK_HEAD,
#line 10021
            .lvl = 64,
#line 10023
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10025
                MOVE_ROCK_SLIDE,
                MOVE_EARTHQUAKE,
                MOVE_CRUNCH,
                MOVE_AERIAL_ACE,
            },
            },
        },
    },
#line 10030
#line 10032
    [DIFFICULTY_NORMAL][TRAINER_PLAYER_SHERRY] =
    {
#line 10031
        .trainerName = _("Sherry"),
#line 10033
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 10034
        .trainerPic = TRAINER_PIC_BRENDAN,
        .encounterMusic_gender =
#line 10036
            TRAINER_ENCOUNTER_MUSIC_ELITE_FOUR,
#line 10038
        .items = { ITEM_FULL_RESTORE },
#line 10037
        .doubleBattle = FALSE,
#line 10039
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_ACE_POKEMON,
#line 10040
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 10042
            .species = SPECIES_EXCADRILL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10042
            .heldItem = ITEM_CLEAR_AMULET,
#line 10046
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10044
            .ability = ABILITY_SAND_FORCE,
#line 10043
            .lvl = 64,
#line 10045
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10047
                MOVE_STRENGTH,
                MOVE_ROCK_SLIDE,
                MOVE_EARTHQUAKE,
                MOVE_METAL_CLAW,
            },
            },
            {
#line 10052
            .species = SPECIES_MIMIKYU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10052
            .heldItem = ITEM_LEFTOVERS,
#line 10056
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10054
            .ability = ABILITY_DISGUISE,
#line 10053
            .lvl = 63,
#line 10055
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10057
                MOVE_SHADOW_CLAW,
                MOVE_PLAY_ROUGH,
                MOVE_HONE_CLAWS,
                MOVE_WOOD_HAMMER,
            },
            },
            {
#line 10062
            .species = SPECIES_ROSERADE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10062
            .heldItem = ITEM_BIG_ROOT,
#line 10066
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10064
            .ability = ABILITY_NATURAL_CURE,
#line 10063
            .lvl = 63,
#line 10065
            .nature = NATURE_TIMID,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10067
                MOVE_GIGA_DRAIN,
                MOVE_GROWTH,
                MOVE_STUN_SPORE,
                MOVE_SLUDGE_BOMB,
            },
            },
            {
#line 10072
            .species = SPECIES_GOTHITELLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10072
            .heldItem = ITEM_PSYCHIC_GEM,
#line 10076
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10074
            .ability = ABILITY_FRISK,
#line 10073
            .lvl = 64,
#line 10075
            .nature = NATURE_TIMID,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10077
                MOVE_SHADOW_BALL,
                MOVE_PSYCHIC,
                MOVE_CALM_MIND,
                MOVE_THUNDERBOLT,
            },
            },
            {
#line 10082
            .species = SPECIES_AERODACTYL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10082
            .heldItem = ITEM_AERODACTYLITE,
#line 10086
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10084
            .ability = ABILITY_ROCK_HEAD,
#line 10083
            .lvl = 64,
#line 10085
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10087
                MOVE_ROCK_SLIDE,
                MOVE_EARTHQUAKE,
                MOVE_CRUNCH,
                MOVE_AERIAL_ACE,
            },
            },
        },
    },
#line 10105
#line 10107
    [DIFFICULTY_EASY][TRAINER_PLAYER_MIKE] =
    {
#line 10106
        .trainerName = _("Mike"),
#line 10108
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 10109
        .trainerPic = TRAINER_PIC_SHUBUBU,
        .encounterMusic_gender =
#line 10111
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 10112
        .doubleBattle = FALSE,
#line 10113
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION,
#line 10114
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 10116
            .species = SPECIES_ARMAROUGE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10116
            .heldItem = ITEM_SHELL_BELL,
#line 10120
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10118
            .ability = ABILITY_FLASH_FIRE,
#line 10117
            .lvl = 66,
#line 10119
            .nature = NATURE_BRAVE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10120
                MOVE_PSYSHOCK,
                MOVE_FLAMETHROWER,
                MOVE_ARMOR_CANNON,
                MOVE_EXPANDING_FORCE,
            },
            },
            {
#line 10125
            .species = SPECIES_LILEEP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10125
            .heldItem = ITEM_ROCKY_HELMET,
#line 10129
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10127
            .ability = ABILITY_SUCTION_CUPS,
#line 10126
            .lvl = 66,
#line 10128
            .nature = NATURE_SASSY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10129
                MOVE_BRINE,
                MOVE_ENERGY_BALL,
                MOVE_GIGA_DRAIN,
                MOVE_ANCIENT_POWER,
            },
            },
            {
#line 10134
            .species = SPECIES_BLASTOISE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10134
            .heldItem = ITEM_BLASTOISINITE,
#line 10138
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10136
            .ability = ABILITY_RAIN_DISH,
#line 10135
            .lvl = 66,
#line 10137
            .nature = NATURE_BASHFUL,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10138
                MOVE_FLASH_CANNON,
                MOVE_WATER_PULSE,
                MOVE_HYDRO_PUMP,
                MOVE_BITE,
            },
            },
            {
#line 10143
            .species = SPECIES_ANNIHILAPE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10143
            .heldItem = ITEM_WIDE_LENS,
#line 10147
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10145
            .ability = ABILITY_DEFIANT,
#line 10144
            .lvl = 66,
#line 10146
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10147
                MOVE_BULK_UP,
                MOVE_BRICK_BREAK,
                MOVE_FOCUS_PUNCH,
                MOVE_SHADOW_PUNCH,
            },
            },
            {
#line 10152
            .species = SPECIES_GOTHITELLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10152
            .heldItem = ITEM_WISE_GLASSES,
#line 10156
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10154
            .ability = ABILITY_FRISK,
#line 10153
            .lvl = 66,
#line 10155
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10156
                MOVE_PSYSHOCK,
                MOVE_PSYCHIC,
                MOVE_CALM_MIND,
                MOVE_FUTURE_SIGHT,
            },
            },
        },
    },
#line 10162
#line 10164
    [DIFFICULTY_NORMAL][TRAINER_PLAYER_MIKE] =
    {
#line 10163
        .trainerName = _("Mike"),
#line 10165
        .trainerClass = TRAINER_CLASS_PKMN_TRAINER_2,
#line 10166
        .trainerPic = TRAINER_PIC_SHUBUBU,
        .encounterMusic_gender =
#line 10168
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 10169
        .doubleBattle = FALSE,
#line 10170
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION,
#line 10171
        .mugshotColor = MUGSHOT_COLOR_PURPLE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 10173
            .species = SPECIES_ARMAROUGE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10173
            .heldItem = ITEM_SHELL_BELL,
#line 10177
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10175
            .ability = ABILITY_FLASH_FIRE,
#line 10174
            .lvl = 66,
#line 10176
            .nature = NATURE_BRAVE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10177
                MOVE_PSYSHOCK,
                MOVE_FLAMETHROWER,
                MOVE_ARMOR_CANNON,
                MOVE_EXPANDING_FORCE,
            },
            },
            {
#line 10182
            .species = SPECIES_LILEEP,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10182
            .heldItem = ITEM_ROCKY_HELMET,
#line 10186
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10184
            .ability = ABILITY_SUCTION_CUPS,
#line 10183
            .lvl = 66,
#line 10185
            .nature = NATURE_SASSY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10186
                MOVE_BRINE,
                MOVE_ENERGY_BALL,
                MOVE_GIGA_DRAIN,
                MOVE_ANCIENT_POWER,
            },
            },
            {
#line 10191
            .species = SPECIES_BLASTOISE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10191
            .heldItem = ITEM_BLASTOISINITE,
#line 10195
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10193
            .ability = ABILITY_RAIN_DISH,
#line 10192
            .lvl = 66,
#line 10194
            .nature = NATURE_BASHFUL,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10195
                MOVE_FLASH_CANNON,
                MOVE_WATER_PULSE,
                MOVE_HYDRO_PUMP,
                MOVE_BITE,
            },
            },
            {
#line 10200
            .species = SPECIES_ANNIHILAPE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10200
            .heldItem = ITEM_WIDE_LENS,
#line 10204
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10202
            .ability = ABILITY_DEFIANT,
#line 10201
            .lvl = 66,
#line 10203
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10204
                MOVE_BULK_UP,
                MOVE_BRICK_BREAK,
                MOVE_FOCUS_PUNCH,
                MOVE_SHADOW_PUNCH,
            },
            },
            {
#line 10209
            .species = SPECIES_GOTHITELLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10209
            .heldItem = ITEM_WISE_GLASSES,
#line 10213
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10211
            .ability = ABILITY_FRISK,
#line 10210
            .lvl = 66,
#line 10212
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10213
                MOVE_PSYSHOCK,
                MOVE_PSYCHIC,
                MOVE_CALM_MIND,
                MOVE_FUTURE_SIGHT,
            },
            },
        },
    },
#line 10233
#line 10235
    [DIFFICULTY_EASY][TRAINER_ROUTE7_A] =
    {
#line 10234
        .trainerName = _("Bella"),
#line 10236
        .trainerClass = TRAINER_CLASS_WAITRESS,
#line 10237
        .trainerPic = TRAINER_PIC_WAITRESS,
        .encounterMusic_gender =
#line 10238
F_TRAINER_FEMALE | 
#line 10239
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 10240
        .doubleBattle = FALSE,
#line 10241
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 10243
            .species = SPECIES_APPLIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10245
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 10244
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 10247
            .species = SPECIES_FLAPPLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10249
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 10248
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 10251
#line 10253
    [DIFFICULTY_NORMAL][TRAINER_ROUTE7_A] =
    {
#line 10252
        .trainerName = _("Bella"),
#line 10254
        .trainerClass = TRAINER_CLASS_WAITRESS,
#line 10255
        .trainerPic = TRAINER_PIC_WAITRESS,
        .encounterMusic_gender =
#line 10256
F_TRAINER_FEMALE | 
#line 10257
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 10258
        .doubleBattle = FALSE,
#line 10259
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 10261
            .species = SPECIES_APPLIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10263
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10262
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 10264
            .species = SPECIES_FLAPPLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10266
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10265
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 10276
#line 10278
    [DIFFICULTY_EASY][TRAINER_ROUTE7_B] =
    {
#line 10277
        .trainerName = _("Galia"),
#line 10279
        .trainerClass = TRAINER_CLASS_BEAUTY,
#line 10280
        .trainerPic = TRAINER_PIC_BEAUTY,
        .encounterMusic_gender =
#line 10281
F_TRAINER_FEMALE | 
#line 10282
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 10283
        .doubleBattle = FALSE,
#line 10284
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 10286
            .species = SPECIES_FURFROU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10288
            .iv = TRAINER_PARTY_IVS(12, 12, 12, 12, 12, 12),
#line 10287
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 10290
#line 10292
    [DIFFICULTY_NORMAL][TRAINER_ROUTE7_B] =
    {
#line 10291
        .trainerName = _("Galia"),
#line 10293
        .trainerClass = TRAINER_CLASS_BEAUTY,
#line 10294
        .trainerPic = TRAINER_PIC_BEAUTY,
        .encounterMusic_gender =
#line 10295
F_TRAINER_FEMALE | 
#line 10296
            TRAINER_ENCOUNTER_MUSIC_RICH,
#line 10297
        .doubleBattle = FALSE,
#line 10298
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 10300
            .species = SPECIES_FURFROU,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10302
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10301
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 10315
#line 10317
    [DIFFICULTY_EASY][TRAINER_ROUTE7_C] =
    {
#line 10316
        .trainerName = _("Shanae"),
#line 10318
        .trainerClass = TRAINER_CLASS_SCHOOL_KID,
#line 10319
        .trainerPic = TRAINER_PIC_SCHOOL_KID_F,
        .encounterMusic_gender =
#line 10320
F_TRAINER_FEMALE | 
#line 10321
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 10322
        .doubleBattle = FALSE,
#line 10323
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 10325
            .species = SPECIES_CHINGLING,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10327
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 10326
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 10329
#line 10331
    [DIFFICULTY_NORMAL][TRAINER_ROUTE7_C] =
    {
#line 10330
        .trainerName = _("Shanae"),
#line 10332
        .trainerClass = TRAINER_CLASS_SCHOOL_KID,
#line 10333
        .trainerPic = TRAINER_PIC_SCHOOL_KID_F,
        .encounterMusic_gender =
#line 10334
F_TRAINER_FEMALE | 
#line 10335
            TRAINER_ENCOUNTER_MUSIC_FEMALE,
#line 10336
        .doubleBattle = FALSE,
#line 10337
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 10339
            .species = SPECIES_CHINGLING,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10341
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10340
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 10355
#line 10357
    [DIFFICULTY_EASY][TRAINER_ROUTE7_D] =
    {
#line 10356
        .trainerName = _("Marcelle"),
#line 10358
        .trainerClass = TRAINER_CLASS_BACKPACKER,
#line 10359
        .trainerPic = TRAINER_PIC_BACKPACKER,
        .encounterMusic_gender =
#line 10361
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 10362
        .doubleBattle = FALSE,
#line 10363
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 10365
            .species = SPECIES_KILOWATTREL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10367
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 10366
            .lvl = 29,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 10369
#line 10371
    [DIFFICULTY_NORMAL][TRAINER_ROUTE7_D] =
    {
#line 10370
        .trainerName = _("Marcelle"),
#line 10372
        .trainerClass = TRAINER_CLASS_BACKPACKER,
#line 10373
        .trainerPic = TRAINER_PIC_BACKPACKER,
        .encounterMusic_gender =
#line 10375
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 10376
        .doubleBattle = FALSE,
#line 10377
        .aiFlags = AI_FLAG_SMART_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 10379
            .species = SPECIES_KILOWATTREL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10381
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10380
            .lvl = 24,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 10395
#line 10397
    [DIFFICULTY_EASY][TRAINER_CHAMPION_GRETA] =
    {
#line 10396
        .trainerName = _("Greta"),
#line 10398
        .trainerClass = TRAINER_CLASS_CHAMPION,
#line 10399
        .trainerPic = TRAINER_PIC_ARENA_TYCOON_GRETA,
        .encounterMusic_gender =
#line 10401
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 10402
        .doubleBattle = FALSE,
#line 10403
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_RISKY,
#line 10404
        .startingStatus = STARTING_STATUS_TRICK_ROOM,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 10406
            .species = SPECIES_CHANDELURE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10406
            .heldItem = ITEM_EXPERT_BELT,
#line 10409
            .ev = TRAINER_PARTY_EVS(252, 0, 0, 0, 252, 0),
#line 10411
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10408
            .ability = ABILITY_FLAME_BODY,
#line 10407
            .lvl = 65,
#line 10410
            .nature = NATURE_QUIET,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10412
                MOVE_MYSTICAL_FIRE,
                MOVE_SHADOW_BALL,
                MOVE_ENERGY_BALL,
                MOVE_CALM_MIND,
            },
            },
            {
#line 10417
            .species = SPECIES_FERALIGATR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10417
            .heldItem = ITEM_LIFE_ORB,
#line 10420
            .ev = TRAINER_PARTY_EVS(96, 252, 12, 0, 0, 148),
#line 10422
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10419
            .ability = ABILITY_SHEER_FORCE,
#line 10418
            .lvl = 66,
#line 10421
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10422
                MOVE_DRAGON_DANCE,
                MOVE_LIQUIDATION,
                MOVE_SUPERPOWER,
                MOVE_STOMPING_TANTRUM,
            },
            },
            {
#line 10427
            .species = SPECIES_ORBEETLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10427
            .heldItem = ITEM_LIGHT_CLAY,
#line 10430
            .ev = TRAINER_PARTY_EVS(252, 0, 4, 0, 252, 0),
#line 10432
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10429
            .ability = ABILITY_SWARM,
#line 10428
            .lvl = 66,
#line 10431
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10433
                MOVE_BUG_BUZZ,
                MOVE_PSYCHIC,
                MOVE_REFLECT,
                MOVE_TRICK_ROOM,
            },
            },
            {
#line 10438
            .species = SPECIES_REVAVROOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10438
            .heldItem = ITEM_WEAKNESS_POLICY,
#line 10441
            .ev = TRAINER_PARTY_EVS(252, 132, 0, 124, 0, 0),
#line 10443
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10440
            .ability = ABILITY_FILTER,
#line 10439
            .lvl = 68,
#line 10442
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10443
                MOVE_SHIFT_GEAR,
                MOVE_GUNK_SHOT,
                MOVE_IRON_HEAD,
                MOVE_SELF_DESTRUCT,
            },
            },
            {
#line 10448
            .species = SPECIES_ROSERADE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10448
            .heldItem = ITEM_POWER_HERB,
#line 10451
            .ev = TRAINER_PARTY_EVS(0, 0, 0, 252, 252, 4),
#line 10453
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10450
            .ability = ABILITY_NATURAL_CURE,
#line 10449
            .lvl = 69,
#line 10452
            .nature = NATURE_TIMID,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10454
                MOVE_SOLAR_BEAM,
                MOVE_SLUDGE_BOMB,
                MOVE_DAZZLING_GLEAM,
                MOVE_SLEEP_POWDER,
            },
            },
            {
#line 10459
            .species = SPECIES_BANETTE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10459
            .heldItem = ITEM_BANETTITE,
#line 10461
            .ev = TRAINER_PARTY_EVS(252, 252, 4, 0, 0, 0),
#line 10463
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10460
            .lvl = 71,
#line 10462
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10463
                MOVE_THUNDER_WAVE,
                MOVE_HEX,
                MOVE_SUCKER_PUNCH,
            },
            },
        },
    },
#line 10467
#line 10469
    [DIFFICULTY_NORMAL][TRAINER_CHAMPION_GRETA] =
    {
#line 10468
        .trainerName = _("Greta"),
#line 10470
        .trainerClass = TRAINER_CLASS_CHAMPION,
#line 10471
        .trainerPic = TRAINER_PIC_ARENA_TYCOON_GRETA,
        .encounterMusic_gender =
#line 10473
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 10474
        .doubleBattle = FALSE,
#line 10475
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_RISKY,
#line 10476
        .startingStatus = STARTING_STATUS_TRICK_ROOM,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 10478
            .species = SPECIES_CHANDELURE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10478
            .heldItem = ITEM_EXPERT_BELT,
#line 10481
            .ev = TRAINER_PARTY_EVS(252, 0, 0, 0, 252, 0),
#line 10483
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10480
            .ability = ABILITY_FLAME_BODY,
#line 10479
            .lvl = 65,
#line 10482
            .nature = NATURE_QUIET,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10484
                MOVE_MYSTICAL_FIRE,
                MOVE_SHADOW_BALL,
                MOVE_ENERGY_BALL,
                MOVE_CALM_MIND,
            },
            },
            {
#line 10489
            .species = SPECIES_FERALIGATR,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10489
            .heldItem = ITEM_LIFE_ORB,
#line 10492
            .ev = TRAINER_PARTY_EVS(96, 252, 12, 0, 0, 148),
#line 10494
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10491
            .ability = ABILITY_SHEER_FORCE,
#line 10490
            .lvl = 66,
#line 10493
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10494
                MOVE_DRAGON_DANCE,
                MOVE_LIQUIDATION,
                MOVE_SUPERPOWER,
                MOVE_STOMPING_TANTRUM,
            },
            },
            {
#line 10499
            .species = SPECIES_ORBEETLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10499
            .heldItem = ITEM_LIGHT_CLAY,
#line 10502
            .ev = TRAINER_PARTY_EVS(252, 0, 4, 0, 252, 0),
#line 10504
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10501
            .ability = ABILITY_SWARM,
#line 10500
            .lvl = 66,
#line 10503
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10505
                MOVE_BUG_BUZZ,
                MOVE_PSYCHIC,
                MOVE_REFLECT,
                MOVE_TRICK_ROOM,
            },
            },
            {
#line 10510
            .species = SPECIES_REVAVROOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10510
            .heldItem = ITEM_WEAKNESS_POLICY,
#line 10513
            .ev = TRAINER_PARTY_EVS(252, 132, 0, 124, 0, 0),
#line 10515
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10512
            .ability = ABILITY_FILTER,
#line 10511
            .lvl = 68,
#line 10514
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10515
                MOVE_SHIFT_GEAR,
                MOVE_GUNK_SHOT,
                MOVE_IRON_HEAD,
                MOVE_SELF_DESTRUCT,
            },
            },
            {
#line 10520
            .species = SPECIES_ROSERADE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10520
            .heldItem = ITEM_POWER_HERB,
#line 10523
            .ev = TRAINER_PARTY_EVS(0, 0, 0, 252, 252, 4),
#line 10525
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10522
            .ability = ABILITY_NATURAL_CURE,
#line 10521
            .lvl = 69,
#line 10524
            .nature = NATURE_TIMID,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10526
                MOVE_SOLAR_BEAM,
                MOVE_SLUDGE_BOMB,
                MOVE_DAZZLING_GLEAM,
                MOVE_SLEEP_POWDER,
            },
            },
            {
#line 10531
            .species = SPECIES_BANETTE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10531
            .heldItem = ITEM_BANETTITE,
#line 10533
            .ev = TRAINER_PARTY_EVS(252, 252, 4, 0, 0, 0),
#line 10535
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10532
            .lvl = 71,
#line 10534
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10535
                MOVE_THUNDER_WAVE,
                MOVE_HEX,
                MOVE_SUCKER_PUNCH,
            },
            },
        },
    },
#line 10539
#line 10541
    [DIFFICULTY_EASY][TRAINER_CHAMPION_RAVINE] =
    {
#line 10540
        .trainerName = _("Ravine"),
#line 10542
        .trainerClass = TRAINER_CLASS_CHAMPION,
#line 10543
        .trainerPic = TRAINER_PIC_DOME_ACE_TUCKER,
        .encounterMusic_gender =
#line 10544
F_TRAINER_FEMALE | 
#line 10545
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 10546
        .doubleBattle = TRUE,
#line 10547
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_RISKY | AI_FLAG_ACE_POKEMON,
#line 10548
        .startingStatus = STARTING_STATUS_RAINBOW_OPPONENT,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 10550
            .species = SPECIES_MASQUERAIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10550
            .heldItem = ITEM_FOCUS_SASH,
#line 10553
            .ev = TRAINER_PARTY_EVS(0, 0, 0, 252, 252, 4),
#line 10555
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10552
            .ability = ABILITY_INTIMIDATE,
#line 10551
            .lvl = 67,
#line 10554
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10556
                MOVE_QUIVER_DANCE,
                MOVE_BUG_BUZZ,
                MOVE_HURRICANE,
                MOVE_SURF,
            },
            },
            {
#line 10561
            .species = SPECIES_SEISMITOAD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10561
            .heldItem = ITEM_LEFTOVERS,
#line 10564
            .ev = TRAINER_PARTY_EVS(252, 4, 164, 0, 0, 88),
#line 10566
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10563
            .ability = ABILITY_WATER_ABSORB,
#line 10562
            .lvl = 68,
#line 10565
            .nature = NATURE_IMPISH,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10566
                MOVE_SURF,
                MOVE_EARTHQUAKE,
                MOVE_STEALTH_ROCK,
                MOVE_KNOCK_OFF,
            },
            },
            {
#line 10571
            .species = SPECIES_MEGANIUM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10571
            .heldItem = ITEM_LEFTOVERS,
#line 10574
            .ev = TRAINER_PARTY_EVS(252, 4, 108, 0, 0, 144),
#line 10576
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10573
            .ability = ABILITY_OVERGROW,
#line 10572
            .lvl = 68,
#line 10575
            .nature = NATURE_SASSY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10576
                MOVE_DRAGON_TAIL,
                MOVE_GIGA_DRAIN,
                MOVE_SYNTHESIS,
                MOVE_TOXIC,
            },
            },
            {
#line 10581
            .species = SPECIES_DUBWOOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10581
            .heldItem = ITEM_ROCKY_HELMET,
#line 10584
            .ev = TRAINER_PARTY_EVS(252, 0, 4, 0, 0, 252),
#line 10586
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10583
            .ability = ABILITY_FLUFFY,
#line 10582
            .lvl = 69,
#line 10585
            .nature = NATURE_CALM,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10587
                MOVE_COTTON_GUARD,
                MOVE_BODY_PRESS,
                MOVE_REST,
                MOVE_SLEEP_TALK,
            },
            },
            {
#line 10592
            .species = SPECIES_LYCANROC_DUSK,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10592
            .heldItem = ITEM_CHOICE_BAND,
#line 10595
            .ev = TRAINER_PARTY_EVS(108, 252, 0, 148, 0, 0),
#line 10597
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10594
            .ability = ABILITY_TOUGH_CLAWS,
#line 10593
            .lvl = 70,
#line 10596
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10597
                MOVE_ACCELEROCK,
                MOVE_CLOSE_COMBAT,
                MOVE_DRILL_RUN,
                MOVE_LAST_RESORT,
            },
            },
            {
#line 10602
            .species = SPECIES_KANGASKHAN,
#line 10602
            .gender = TRAINER_MON_FEMALE,
#line 10602
            .heldItem = ITEM_KANGASKHANITE,
#line 10605
            .ev = TRAINER_PARTY_EVS(252, 0, 32, 96, 0, 128),
#line 10607
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10604
            .ability = ABILITY_PARENTAL_BOND,
#line 10603
            .lvl = 73,
#line 10606
            .nature = NATURE_IMPISH,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10607
                MOVE_FAKE_OUT,
                MOVE_POWER_UP_PUNCH,
                MOVE_LAST_RESORT,
                MOVE_CRUNCH,
            },
            },
        },
    },
#line 10612
#line 10614
    [DIFFICULTY_NORMAL][TRAINER_CHAMPION_RAVINE] =
    {
#line 10613
        .trainerName = _("Ravine"),
#line 10615
        .trainerClass = TRAINER_CLASS_CHAMPION,
#line 10616
        .trainerPic = TRAINER_PIC_DOME_ACE_TUCKER,
        .encounterMusic_gender =
#line 10617
F_TRAINER_FEMALE | 
#line 10618
            TRAINER_ENCOUNTER_MUSIC_GIRL,
#line 10619
        .doubleBattle = TRUE,
#line 10620
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_RISKY | AI_FLAG_ACE_POKEMON,
#line 10621
        .startingStatus = STARTING_STATUS_RAINBOW_OPPONENT,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 10623
            .species = SPECIES_MASQUERAIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10623
            .heldItem = ITEM_FOCUS_SASH,
#line 10626
            .ev = TRAINER_PARTY_EVS(0, 0, 0, 252, 252, 4),
#line 10628
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10625
            .ability = ABILITY_INTIMIDATE,
#line 10624
            .lvl = 67,
#line 10627
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10629
                MOVE_QUIVER_DANCE,
                MOVE_BUG_BUZZ,
                MOVE_HURRICANE,
                MOVE_SURF,
            },
            },
            {
#line 10634
            .species = SPECIES_SEISMITOAD,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10634
            .heldItem = ITEM_LEFTOVERS,
#line 10637
            .ev = TRAINER_PARTY_EVS(252, 4, 164, 0, 0, 88),
#line 10639
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10636
            .ability = ABILITY_WATER_ABSORB,
#line 10635
            .lvl = 68,
#line 10638
            .nature = NATURE_IMPISH,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10639
                MOVE_SURF,
                MOVE_EARTHQUAKE,
                MOVE_STEALTH_ROCK,
                MOVE_KNOCK_OFF,
            },
            },
            {
#line 10644
            .species = SPECIES_MEGANIUM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10644
            .heldItem = ITEM_LEFTOVERS,
#line 10647
            .ev = TRAINER_PARTY_EVS(252, 4, 108, 0, 0, 144),
#line 10649
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10646
            .ability = ABILITY_OVERGROW,
#line 10645
            .lvl = 68,
#line 10648
            .nature = NATURE_SASSY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10649
                MOVE_DRAGON_TAIL,
                MOVE_GIGA_DRAIN,
                MOVE_SYNTHESIS,
                MOVE_TOXIC,
            },
            },
            {
#line 10654
            .species = SPECIES_DUBWOOL,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10654
            .heldItem = ITEM_ROCKY_HELMET,
#line 10657
            .ev = TRAINER_PARTY_EVS(252, 0, 4, 0, 0, 252),
#line 10659
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10656
            .ability = ABILITY_FLUFFY,
#line 10655
            .lvl = 69,
#line 10658
            .nature = NATURE_CALM,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10660
                MOVE_COTTON_GUARD,
                MOVE_BODY_PRESS,
                MOVE_REST,
                MOVE_SLEEP_TALK,
            },
            },
            {
#line 10665
            .species = SPECIES_LYCANROC_DUSK,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10665
            .heldItem = ITEM_CHOICE_BAND,
#line 10668
            .ev = TRAINER_PARTY_EVS(108, 252, 0, 148, 0, 0),
#line 10670
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10667
            .ability = ABILITY_TOUGH_CLAWS,
#line 10666
            .lvl = 70,
#line 10669
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10670
                MOVE_ACCELEROCK,
                MOVE_CLOSE_COMBAT,
                MOVE_DRILL_RUN,
                MOVE_LAST_RESORT,
            },
            },
            {
#line 10675
            .species = SPECIES_KANGASKHAN,
#line 10675
            .gender = TRAINER_MON_FEMALE,
#line 10675
            .heldItem = ITEM_KANGASKHANITE,
#line 10678
            .ev = TRAINER_PARTY_EVS(252, 0, 32, 96, 0, 128),
#line 10680
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10677
            .ability = ABILITY_PARENTAL_BOND,
#line 10676
            .lvl = 73,
#line 10679
            .nature = NATURE_IMPISH,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10680
                MOVE_FAKE_OUT,
                MOVE_POWER_UP_PUNCH,
                MOVE_LAST_RESORT,
                MOVE_CRUNCH,
            },
            },
        },
    },
#line 10686
#line 10688
    [DIFFICULTY_EASY][TRAINER_CHAMPION_LYNCH] =
    {
#line 10687
        .trainerName = _("Lynch"),
#line 10689
        .trainerClass = TRAINER_CLASS_CHAMPION,
#line 10690
        .trainerPic = TRAINER_PIC_CHAMPION_LYNCH,
        .encounterMusic_gender =
#line 10692
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 10693
        .doubleBattle = FALSE,
#line 10694
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_RISKY | AI_FLAG_ACE_POKEMON,
#line 10695
        .startingStatus = STARTING_STATUS_RAINBOW_OPPONENT,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 10697
            .species = SPECIES_AMOONGUSS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10697
            .heldItem = ITEM_LEFTOVERS,
#line 10700
            .ev = TRAINER_PARTY_EVS(252, 0, 88, 44, 0, 124),
#line 10702
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10699
            .ability = ABILITY_REGENERATOR,
#line 10698
            .lvl = 69,
#line 10701
            .nature = NATURE_SASSY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10702
                MOVE_SPORE,
                MOVE_SLUDGE_BOMB,
                MOVE_ENERGY_BALL,
                MOVE_STOMPING_TANTRUM,
            },
            },
            {
#line 10707
            .species = SPECIES_TALONFLAME,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10707
            .heldItem = ITEM_LIECHI_BERRY,
#line 10710
            .ev = TRAINER_PARTY_EVS(248, 8, 0, 252, 0, 0),
#line 10712
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10709
            .ability = ABILITY_GALE_WINGS,
#line 10708
            .lvl = 70,
#line 10711
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10712
                MOVE_BRAVE_BIRD,
                MOVE_WILL_O_WISP,
                MOVE_FLARE_BLITZ,
                MOVE_ROOST,
            },
            },
            {
#line 10717
            .species = SPECIES_SINISTCHA_MASTERPIECE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10717
            .heldItem = ITEM_BIG_ROOT,
#line 10720
            .ev = TRAINER_PARTY_EVS(252, 0, 0, 0, 252, 4),
#line 10722
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10719
            .ability = ABILITY_HEATPROOF,
#line 10718
            .lvl = 70,
#line 10721
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10723
                MOVE_MATCHA_GOTCHA,
                MOVE_CALM_MIND,
                MOVE_SHADOW_BALL,
                MOVE_STRENGTH_SAP,
            },
            },
            {
#line 10728
            .species = SPECIES_LOPUNNY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10728
            .heldItem = ITEM_LOPUNNITE,
#line 10731
            .ev = TRAINER_PARTY_EVS(0, 252, 0, 252, 0, 4),
#line 10733
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10730
            .ability = ABILITY_LIMBER,
#line 10729
            .lvl = 73,
#line 10732
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10733
                MOVE_FAKE_OUT,
                MOVE_HI_JUMP_KICK,
                MOVE_QUICK_ATTACK,
                MOVE_POWER_UP_PUNCH,
            },
            },
            {
#line 10738
            .species = SPECIES_BRUXISH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10738
            .heldItem = ITEM_LIFE_ORB,
#line 10741
            .ev = TRAINER_PARTY_EVS(0, 252, 0, 252, 0, 4),
#line 10743
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10740
            .ability = ABILITY_STRONG_JAW,
#line 10739
            .lvl = 72,
#line 10742
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10743
                MOVE_PSYCHIC_FANGS,
                MOVE_LIQUIDATION,
                MOVE_CRUNCH,
                MOVE_ICE_FANG,
            },
            },
            {
#line 10748
            .species = SPECIES_HYDRAPPLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10748
            .heldItem = ITEM_LIFE_ORB,
#line 10751
            .ev = TRAINER_PARTY_EVS(248, 0, 0, 0, 252, 8),
#line 10753
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10750
            .ability = ABILITY_REGENERATOR,
#line 10749
            .lvl = 75,
#line 10752
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10754
                MOVE_FICKLE_BEAM,
                MOVE_ENERGY_BALL,
                MOVE_NASTY_PLOT,
                MOVE_EARTH_POWER,
            },
            },
        },
    },
#line 10759
#line 10761
    [DIFFICULTY_NORMAL][TRAINER_CHAMPION_LYNCH] =
    {
#line 10760
        .trainerName = _("Lynch"),
#line 10762
        .trainerClass = TRAINER_CLASS_CHAMPION,
#line 10763
        .trainerPic = TRAINER_PIC_CHAMPION_LYNCH,
        .encounterMusic_gender =
#line 10765
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 10766
        .doubleBattle = FALSE,
#line 10767
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_RISKY | AI_FLAG_ACE_POKEMON,
#line 10768
        .startingStatus = STARTING_STATUS_RAINBOW_OPPONENT,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 10770
            .species = SPECIES_AMOONGUSS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10770
            .heldItem = ITEM_LEFTOVERS,
#line 10773
            .ev = TRAINER_PARTY_EVS(252, 0, 88, 44, 0, 124),
#line 10775
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10772
            .ability = ABILITY_REGENERATOR,
#line 10771
            .lvl = 69,
#line 10774
            .nature = NATURE_SASSY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10775
                MOVE_SPORE,
                MOVE_SLUDGE_BOMB,
                MOVE_ENERGY_BALL,
                MOVE_STOMPING_TANTRUM,
            },
            },
            {
#line 10780
            .species = SPECIES_TALONFLAME,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10780
            .heldItem = ITEM_LIECHI_BERRY,
#line 10783
            .ev = TRAINER_PARTY_EVS(248, 8, 0, 252, 0, 0),
#line 10785
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10782
            .ability = ABILITY_GALE_WINGS,
#line 10781
            .lvl = 70,
#line 10784
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10785
                MOVE_BRAVE_BIRD,
                MOVE_WILL_O_WISP,
                MOVE_FLARE_BLITZ,
                MOVE_ROOST,
            },
            },
            {
#line 10790
            .species = SPECIES_SINISTCHA_MASTERPIECE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10790
            .heldItem = ITEM_BIG_ROOT,
#line 10793
            .ev = TRAINER_PARTY_EVS(252, 0, 0, 0, 252, 4),
#line 10795
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10792
            .ability = ABILITY_HEATPROOF,
#line 10791
            .lvl = 70,
#line 10794
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10796
                MOVE_MATCHA_GOTCHA,
                MOVE_CALM_MIND,
                MOVE_SHADOW_BALL,
                MOVE_STRENGTH_SAP,
            },
            },
            {
#line 10801
            .species = SPECIES_LOPUNNY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10801
            .heldItem = ITEM_LOPUNNITE,
#line 10804
            .ev = TRAINER_PARTY_EVS(0, 252, 0, 252, 0, 4),
#line 10806
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10803
            .ability = ABILITY_LIMBER,
#line 10802
            .lvl = 73,
#line 10805
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10806
                MOVE_FAKE_OUT,
                MOVE_HI_JUMP_KICK,
                MOVE_QUICK_ATTACK,
                MOVE_POWER_UP_PUNCH,
            },
            },
            {
#line 10811
            .species = SPECIES_BRUXISH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10811
            .heldItem = ITEM_LIFE_ORB,
#line 10814
            .ev = TRAINER_PARTY_EVS(0, 252, 0, 252, 0, 4),
#line 10816
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10813
            .ability = ABILITY_STRONG_JAW,
#line 10812
            .lvl = 72,
#line 10815
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10816
                MOVE_PSYCHIC_FANGS,
                MOVE_LIQUIDATION,
                MOVE_CRUNCH,
                MOVE_ICE_FANG,
            },
            },
            {
#line 10821
            .species = SPECIES_HYDRAPPLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10821
            .heldItem = ITEM_LIFE_ORB,
#line 10824
            .ev = TRAINER_PARTY_EVS(248, 0, 0, 0, 252, 8),
#line 10826
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10823
            .ability = ABILITY_REGENERATOR,
#line 10822
            .lvl = 75,
#line 10825
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10827
                MOVE_FICKLE_BEAM,
                MOVE_ENERGY_BALL,
                MOVE_NASTY_PLOT,
                MOVE_EARTH_POWER,
            },
            },
        },
    },
#line 10832
#line 10834
    [DIFFICULTY_EASY][TRAINER_CHAMPION_MARTHA] =
    {
#line 10833
        .trainerName = _("Martha"),
#line 10835
        .trainerClass = TRAINER_CLASS_CHAMPION,
#line 10836
        .trainerPic = TRAINER_PIC_EXPERT_F,
        .encounterMusic_gender =
#line 10838
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 10839
        .doubleBattle = TRUE,
#line 10840
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_RISKY | AI_FLAG_ACE_POKEMON,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 10842
            .species = SPECIES_AURORUS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10842
            .heldItem = ITEM_LIGHT_CLAY,
#line 10845
            .ev = TRAINER_PARTY_EVS(252, 0, 144, 0, 0, 112),
#line 10847
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10844
            .ability = ABILITY_SNOW_WARNING,
#line 10843
            .lvl = 70,
#line 10846
            .nature = NATURE_CALM,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10848
                MOVE_BLIZZARD,
                MOVE_AURORA_VEIL,
                MOVE_ANCIENT_POWER,
                MOVE_EARTH_POWER,
            },
            },
            {
#line 10853
            .species = SPECIES_FROSMOTH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10853
            .heldItem = ITEM_LIFE_ORB,
#line 10856
            .ev = TRAINER_PARTY_EVS(0, 0, 0, 252, 252, 4),
#line 10858
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10855
            .ability = ABILITY_ICE_SCALES,
#line 10854
            .lvl = 72,
#line 10857
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10859
                MOVE_QUIVER_DANCE,
                MOVE_BUG_BUZZ,
                MOVE_BLIZZARD,
                MOVE_DAZZLING_GLEAM,
            },
            },
            {
#line 10864
            .species = SPECIES_ARCANINE_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10864
            .heldItem = ITEM_CHOICE_BAND,
#line 10867
            .ev = TRAINER_PARTY_EVS(0, 252, 0, 252, 0, 4),
#line 10869
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10866
            .ability = ABILITY_INTIMIDATE,
#line 10865
            .lvl = 74,
#line 10868
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10869
                MOVE_EXTREME_SPEED,
                MOVE_ROCK_SLIDE,
                MOVE_FLARE_BLITZ,
                MOVE_WILD_CHARGE,
            },
            },
            {
#line 10874
            .species = SPECIES_GOODRA_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10874
            .heldItem = ITEM_LEFTOVERS,
#line 10877
            .ev = TRAINER_PARTY_EVS(252, 4, 252, 0, 0, 0),
#line 10879
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10876
            .ability = ABILITY_SAP_SIPPER,
#line 10875
            .lvl = 73,
#line 10878
            .nature = NATURE_CAREFUL,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10879
                MOVE_BODY_PRESS,
                MOVE_BREAKING_SWIPE,
                MOVE_LIFE_DEW,
                MOVE_KNOCK_OFF,
            },
            },
            {
#line 10884
            .species = SPECIES_MR_RIME,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10884
            .heldItem = ITEM_LIFE_ORB,
#line 10887
            .ev = TRAINER_PARTY_EVS(248, 0, 0, 0, 252, 8),
#line 10889
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10886
            .ability = ABILITY_ICE_BODY,
#line 10885
            .lvl = 73,
#line 10888
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10890
                MOVE_FREEZE_DRY,
                MOVE_BLIZZARD,
                MOVE_FUTURE_SIGHT,
                MOVE_SLACK_OFF,
            },
            },
            {
#line 10895
            .species = SPECIES_HOUNDSTONE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10895
            .heldItem = ITEM_SITRUS_BERRY,
#line 10898
            .ev = TRAINER_PARTY_EVS(0, 252, 0, 252, 0, 0),
#line 10900
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10897
            .ability = ABILITY_FLUFFY,
#line 10896
            .lvl = 77,
#line 10899
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10900
                MOVE_LAST_RESPECTS,
                MOVE_CRUNCH,
            },
            },
        },
    },
#line 10903
#line 10905
    [DIFFICULTY_NORMAL][TRAINER_CHAMPION_MARTHA] =
    {
#line 10904
        .trainerName = _("Martha"),
#line 10906
        .trainerClass = TRAINER_CLASS_CHAMPION,
#line 10907
        .trainerPic = TRAINER_PIC_EXPERT_F,
        .encounterMusic_gender =
#line 10909
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 10910
        .doubleBattle = TRUE,
#line 10911
        .aiFlags = AI_FLAG_SMART_TRAINER | AI_FLAG_PREDICTION | AI_FLAG_RISKY | AI_FLAG_ACE_POKEMON,
        .partySize = 6,
        .party = (const struct TrainerMon[])
        {
            {
#line 10913
            .species = SPECIES_AURORUS,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10913
            .heldItem = ITEM_LIGHT_CLAY,
#line 10916
            .ev = TRAINER_PARTY_EVS(252, 0, 144, 0, 0, 112),
#line 10918
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10915
            .ability = ABILITY_SNOW_WARNING,
#line 10914
            .lvl = 70,
#line 10917
            .nature = NATURE_CALM,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10919
                MOVE_BLIZZARD,
                MOVE_AURORA_VEIL,
                MOVE_ANCIENT_POWER,
                MOVE_EARTH_POWER,
            },
            },
            {
#line 10924
            .species = SPECIES_FROSMOTH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10924
            .heldItem = ITEM_LIFE_ORB,
#line 10927
            .ev = TRAINER_PARTY_EVS(0, 0, 0, 252, 252, 4),
#line 10929
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10926
            .ability = ABILITY_ICE_SCALES,
#line 10925
            .lvl = 72,
#line 10928
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10930
                MOVE_QUIVER_DANCE,
                MOVE_BUG_BUZZ,
                MOVE_BLIZZARD,
                MOVE_DAZZLING_GLEAM,
            },
            },
            {
#line 10935
            .species = SPECIES_ARCANINE_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10935
            .heldItem = ITEM_CHOICE_BAND,
#line 10938
            .ev = TRAINER_PARTY_EVS(0, 252, 0, 252, 0, 4),
#line 10940
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10937
            .ability = ABILITY_INTIMIDATE,
#line 10936
            .lvl = 74,
#line 10939
            .nature = NATURE_JOLLY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10940
                MOVE_EXTREME_SPEED,
                MOVE_ROCK_SLIDE,
                MOVE_FLARE_BLITZ,
                MOVE_WILD_CHARGE,
            },
            },
            {
#line 10945
            .species = SPECIES_GOODRA_HISUI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10945
            .heldItem = ITEM_LEFTOVERS,
#line 10948
            .ev = TRAINER_PARTY_EVS(252, 4, 252, 0, 0, 0),
#line 10950
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10947
            .ability = ABILITY_SAP_SIPPER,
#line 10946
            .lvl = 73,
#line 10949
            .nature = NATURE_CAREFUL,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10950
                MOVE_BODY_PRESS,
                MOVE_BREAKING_SWIPE,
                MOVE_LIFE_DEW,
                MOVE_KNOCK_OFF,
            },
            },
            {
#line 10955
            .species = SPECIES_MR_RIME,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10955
            .heldItem = ITEM_LIFE_ORB,
#line 10958
            .ev = TRAINER_PARTY_EVS(248, 0, 0, 0, 252, 8),
#line 10960
            .iv = TRAINER_PARTY_IVS(31, 0, 31, 31, 31, 31),
#line 10957
            .ability = ABILITY_ICE_BODY,
#line 10956
            .lvl = 73,
#line 10959
            .nature = NATURE_MODEST,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10961
                MOVE_FREEZE_DRY,
                MOVE_BLIZZARD,
                MOVE_FUTURE_SIGHT,
                MOVE_SLACK_OFF,
            },
            },
            {
#line 10966
            .species = SPECIES_HOUNDSTONE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10966
            .heldItem = ITEM_SITRUS_BERRY,
#line 10969
            .ev = TRAINER_PARTY_EVS(0, 252, 0, 252, 0, 0),
#line 10971
            .iv = TRAINER_PARTY_IVS(31, 31, 31, 31, 31, 31),
#line 10968
            .ability = ABILITY_FLUFFY,
#line 10967
            .lvl = 77,
#line 10970
            .nature = NATURE_ADAMANT,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 10971
                MOVE_LAST_RESPECTS,
                MOVE_CRUNCH,
            },
            },
        },
    },
#line 10974
    [DIFFICULTY_NORMAL][TRAINER_VICTORYCAPE_AREY_1] =
    {
#line 10975
        .trainerName = _("JEFFREY"),
#line 10976
        .trainerClass = TRAINER_CLASS_BUG_MANIAC,
#line 10977
        .trainerPic = TRAINER_PIC_BUG_MANIAC,
        .encounterMusic_gender =
#line 10979
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 10980
        .doubleBattle = FALSE,
#line 10981
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 10983
            .species = SPECIES_SURSKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10985
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 10984
            .lvl = 27,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 10987
            .species = SPECIES_SURSKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10989
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 10988
            .lvl = 27,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 10991
            .species = SPECIES_SURSKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 10993
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 10992
            .lvl = 27,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 10995
    [DIFFICULTY_NORMAL][TRAINER_VICTORYCAPE_AREY_2] =
    {
#line 10996
        .trainerName = _("JEFFREY"),
#line 10997
        .trainerClass = TRAINER_CLASS_BUG_MANIAC,
#line 10998
        .trainerPic = TRAINER_PIC_BUG_MANIAC,
        .encounterMusic_gender =
#line 11000
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 11001
        .doubleBattle = FALSE,
#line 11002
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 11004
            .species = SPECIES_SURSKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11006
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 11005
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11008
            .species = SPECIES_SURSKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11010
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 11009
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11012
            .species = SPECIES_SURSKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11014
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 11013
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11016
    [DIFFICULTY_NORMAL][TRAINER_VICTORYCAPE_AREY_3] =
    {
#line 11017
        .trainerName = _("JEFFREY"),
#line 11018
        .trainerClass = TRAINER_CLASS_BUG_MANIAC,
#line 11019
        .trainerPic = TRAINER_PIC_BUG_MANIAC,
        .encounterMusic_gender =
#line 11021
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 11022
        .doubleBattle = FALSE,
#line 11023
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 3,
        .party = (const struct TrainerMon[])
        {
            {
#line 11025
            .species = SPECIES_SURSKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11027
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 11026
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11029
            .species = SPECIES_SURSKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11031
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 11030
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11033
            .species = SPECIES_MASQUERAIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11035
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 11034
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11037
    [DIFFICULTY_NORMAL][TRAINER_VICTORYCAPE_AREY_4] =
    {
#line 11038
        .trainerName = _("JEFFREY"),
#line 11039
        .trainerClass = TRAINER_CLASS_BUG_MANIAC,
#line 11040
        .trainerPic = TRAINER_PIC_BUG_MANIAC,
        .encounterMusic_gender =
#line 11042
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 11043
        .doubleBattle = FALSE,
#line 11044
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 4,
        .party = (const struct TrainerMon[])
        {
            {
#line 11046
            .species = SPECIES_SURSKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11048
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 11047
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11050
            .species = SPECIES_WURMPLE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11052
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 11051
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11054
            .species = SPECIES_SURSKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11056
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 11055
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11058
            .species = SPECIES_MASQUERAIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11060
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 11059
            .lvl = 36,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11062
    [DIFFICULTY_NORMAL][TRAINER_VICTORYCAPE_AREY_5] =
    {
#line 11063
        .trainerName = _("JEFFREY"),
#line 11064
        .trainerClass = TRAINER_CLASS_BUG_MANIAC,
#line 11065
        .trainerPic = TRAINER_PIC_BUG_MANIAC,
        .encounterMusic_gender =
#line 11067
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 11068
        .doubleBattle = FALSE,
#line 11069
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 5,
        .party = (const struct TrainerMon[])
        {
            {
#line 11071
            .species = SPECIES_SURSKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11073
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 11072
            .lvl = 38,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11075
            .species = SPECIES_DUSTOX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11077
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 11076
            .lvl = 38,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11079
            .species = SPECIES_SURSKIT,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11081
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 11080
            .lvl = 38,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11083
            .species = SPECIES_MASQUERAIN,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11083
            .heldItem = ITEM_SILVER_POWDER,
#line 11085
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 11084
            .lvl = 38,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11087
            .species = SPECIES_BEAUTIFLY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11089
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 11088
            .lvl = 38,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11091
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_AI_1] =
    {
#line 11092
        .trainerName = _("JACKI"),
#line 11093
        .trainerClass = TRAINER_CLASS_PSYCHIC,
#line 11094
        .trainerPic = TRAINER_PIC_PSYCHIC_F,
        .encounterMusic_gender =
#line 11095
F_TRAINER_FEMALE | 
#line 11096
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 11097
        .doubleBattle = FALSE,
#line 11098
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11100
            .species = SPECIES_KADABRA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11102
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11101
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11104
            .species = SPECIES_LUNATONE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11106
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11105
            .lvl = 30,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11108
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_AI_2] =
    {
#line 11109
        .trainerName = _("JACKI"),
#line 11110
        .trainerClass = TRAINER_CLASS_PSYCHIC,
#line 11111
        .trainerPic = TRAINER_PIC_PSYCHIC_F,
        .encounterMusic_gender =
#line 11112
F_TRAINER_FEMALE | 
#line 11113
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 11114
        .doubleBattle = FALSE,
#line 11115
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11117
            .species = SPECIES_KADABRA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11119
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 11118
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11121
            .species = SPECIES_LUNATONE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11123
            .iv = TRAINER_PARTY_IVS(1, 1, 1, 1, 1, 1),
#line 11122
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11125
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_AI_3] =
    {
#line 11126
        .trainerName = _("JACKI"),
#line 11127
        .trainerClass = TRAINER_CLASS_PSYCHIC,
#line 11128
        .trainerPic = TRAINER_PIC_PSYCHIC_F,
        .encounterMusic_gender =
#line 11129
F_TRAINER_FEMALE | 
#line 11130
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 11131
        .doubleBattle = FALSE,
#line 11132
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11134
            .species = SPECIES_KADABRA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11136
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 11135
            .lvl = 37,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11138
            .species = SPECIES_LUNATONE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11140
            .iv = TRAINER_PARTY_IVS(2, 2, 2, 2, 2, 2),
#line 11139
            .lvl = 37,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11142
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_AI_4] =
    {
#line 11143
        .trainerName = _("JACKI"),
#line 11144
        .trainerClass = TRAINER_CLASS_PSYCHIC,
#line 11145
        .trainerPic = TRAINER_PIC_PSYCHIC_F,
        .encounterMusic_gender =
#line 11146
F_TRAINER_FEMALE | 
#line 11147
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 11148
        .doubleBattle = FALSE,
#line 11149
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11151
            .species = SPECIES_KADABRA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11153
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 11152
            .lvl = 40,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11155
            .species = SPECIES_LUNATONE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11157
            .iv = TRAINER_PARTY_IVS(3, 3, 3, 3, 3, 3),
#line 11156
            .lvl = 40,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11159
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_AI_5] =
    {
#line 11160
        .trainerName = _("JACKI"),
#line 11161
        .trainerClass = TRAINER_CLASS_PSYCHIC,
#line 11162
        .trainerPic = TRAINER_PIC_PSYCHIC_F,
        .encounterMusic_gender =
#line 11163
F_TRAINER_FEMALE | 
#line 11164
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 11165
        .doubleBattle = FALSE,
#line 11166
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11168
            .species = SPECIES_LUNATONE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11170
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 11169
            .lvl = 43,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11172
            .species = SPECIES_ALAKAZAM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11174
            .iv = TRAINER_PARTY_IVS(4, 4, 4, 4, 4, 4),
#line 11173
            .lvl = 43,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11176
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_ASON_1] =
    {
#line 11177
        .trainerName = _("JACKSON"),
#line 11178
        .trainerClass = TRAINER_CLASS_PKMN_RANGER,
#line 11179
        .trainerPic = TRAINER_PIC_POKEMON_RANGER_M,
        .encounterMusic_gender =
#line 11181
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 11182
        .items = { ITEM_FULL_RESTORE },
#line 11183
        .doubleBattle = FALSE,
#line 11184
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 11186
            .species = SPECIES_BRELOOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11188
            .iv = TRAINER_PARTY_IVS(6, 6, 6, 6, 6, 6),
#line 11187
            .lvl = 27,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11190
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_ASON_2] =
    {
#line 11191
        .trainerName = _("JACKSON"),
#line 11192
        .trainerClass = TRAINER_CLASS_PKMN_RANGER,
#line 11193
        .trainerPic = TRAINER_PIC_POKEMON_RANGER_M,
        .encounterMusic_gender =
#line 11195
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 11196
        .items = { ITEM_FULL_RESTORE },
#line 11197
        .doubleBattle = FALSE,
#line 11198
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE | AI_FLAG_TRY_TO_FAINT | AI_FLAG_FORCE_SETUP_FIRST_TURN,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 11200
            .species = SPECIES_BRELOOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11202
            .iv = TRAINER_PARTY_IVS(7, 7, 7, 7, 7, 7),
#line 11201
            .lvl = 31,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11204
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_ASON_3] =
    {
#line 11205
        .trainerName = _("JACKSON"),
#line 11206
        .trainerClass = TRAINER_CLASS_PKMN_RANGER,
#line 11207
        .trainerPic = TRAINER_PIC_POKEMON_RANGER_M,
        .encounterMusic_gender =
#line 11209
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 11210
        .items = { ITEM_FULL_RESTORE },
#line 11211
        .doubleBattle = FALSE,
#line 11212
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 11214
            .species = SPECIES_BRELOOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11216
            .iv = TRAINER_PARTY_IVS(8, 8, 8, 8, 8, 8),
#line 11215
            .lvl = 34,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11218
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_ASON_4] =
    {
#line 11219
        .trainerName = _("JACKSON"),
#line 11220
        .trainerClass = TRAINER_CLASS_PKMN_RANGER,
#line 11221
        .trainerPic = TRAINER_PIC_POKEMON_RANGER_M,
        .encounterMusic_gender =
#line 11223
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 11224
        .items = { ITEM_FULL_RESTORE },
#line 11225
        .doubleBattle = FALSE,
#line 11226
        .aiFlags = AI_FLAG_CHECK_BAD_MOVE | AI_FLAG_TRY_TO_FAINT | AI_FLAG_FORCE_SETUP_FIRST_TURN,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 11228
            .species = SPECIES_BRELOOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11230
            .iv = TRAINER_PARTY_IVS(9, 9, 9, 9, 9, 9),
#line 11229
            .lvl = 37,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11232
    [DIFFICULTY_NORMAL][TRAINER_UNCHARTED_ISLAND_GRUNT_ASON_5] =
    {
#line 11233
        .trainerName = _("JACKSON"),
#line 11234
        .trainerClass = TRAINER_CLASS_PKMN_RANGER,
#line 11235
        .trainerPic = TRAINER_PIC_POKEMON_RANGER_M,
        .encounterMusic_gender =
#line 11237
            TRAINER_ENCOUNTER_MUSIC_COOL,
#line 11238
        .items = { ITEM_FULL_RESTORE },
#line 11239
        .doubleBattle = FALSE,
#line 11240
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11242
            .species = SPECIES_KECLEON,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11244
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 11243
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11246
            .species = SPECIES_BRELOOM,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11248
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 11247
            .lvl = 39,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11250
#line 11252
    [DIFFICULTY_EASY][TRAINER_DR_EDEN_LAB_1] =
    {
#line 11251
        .trainerName = _("???"),
#line 11253
        .trainerClass = TRAINER_CLASS_BRIGAND,
#line 11254
        .trainerPic = TRAINER_PIC_EDEN,
        .encounterMusic_gender =
#line 11255
F_TRAINER_FEMALE | 
#line 11256
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 11257
        .doubleBattle = FALSE,
#line 11258
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11260
            .nickname = COMPOUND_STRING("Pilfer"),
#line 11260
            .species = SPECIES_NICKIT,
#line 11260
            .gender = TRAINER_MON_MALE,
#line 11264
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11262
            .ability = ABILITY_PRANKSTER,
#line 11261
            .lvl = 5,
            .nature = NATURE_HARDY,
#line 11263
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 11265
                MOVE_TAIL_WHIP,
                MOVE_FAKE_TEARS,
                MOVE_BEAT_UP,
                MOVE_TACKLE,
            },
            },
            {
#line 11270
            .species = SPECIES_TINKATINK,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11272
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11271
            .lvl = 5,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11274
#line 11276
    [DIFFICULTY_EASY][TRAINER_DR_EDEN_LAB_2] =
    {
#line 11275
        .trainerName = _("???"),
#line 11277
        .trainerClass = TRAINER_CLASS_BRIGAND,
#line 11278
        .trainerPic = TRAINER_PIC_EDEN,
        .encounterMusic_gender =
#line 11279
F_TRAINER_FEMALE | 
#line 11280
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 11281
        .doubleBattle = FALSE,
#line 11282
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11284
            .nickname = COMPOUND_STRING("Pilfer"),
#line 11284
            .species = SPECIES_NICKIT,
#line 11284
            .gender = TRAINER_MON_MALE,
#line 11288
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11286
            .ability = ABILITY_PRANKSTER,
#line 11285
            .lvl = 5,
            .nature = NATURE_HARDY,
#line 11287
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 11289
                MOVE_TAIL_WHIP,
                MOVE_FAKE_TEARS,
                MOVE_BEAT_UP,
                MOVE_TACKLE,
            },
            },
            {
#line 11294
            .species = SPECIES_FRIGIBAX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11297
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11295
            .lvl = 5,
            .nature = NATURE_HARDY,
#line 11296
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11299
#line 11301
    [DIFFICULTY_EASY][TRAINER_DR_EDEN_LAB_3] =
    {
#line 11300
        .trainerName = _("???"),
#line 11302
        .trainerClass = TRAINER_CLASS_BRIGAND,
#line 11303
        .trainerPic = TRAINER_PIC_EDEN,
        .encounterMusic_gender =
#line 11304
F_TRAINER_FEMALE | 
#line 11305
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 11306
        .doubleBattle = FALSE,
#line 11307
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11309
            .nickname = COMPOUND_STRING("Pilfer"),
#line 11309
            .species = SPECIES_NICKIT,
#line 11309
            .gender = TRAINER_MON_MALE,
#line 11313
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11311
            .ability = ABILITY_PRANKSTER,
#line 11310
            .lvl = 5,
            .nature = NATURE_HARDY,
#line 11312
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 11314
                MOVE_TAIL_WHIP,
                MOVE_FAKE_TEARS,
                MOVE_BEAT_UP,
                MOVE_TACKLE,
            },
            },
            {
#line 11319
            .species = SPECIES_TEDDIURSA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11321
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11320
            .lvl = 5,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11323
#line 11325
    [DIFFICULTY_NORMAL][TRAINER_DR_EDEN_LAB_1] =
    {
#line 11324
        .trainerName = _("???"),
#line 11326
        .trainerClass = TRAINER_CLASS_BRIGAND,
#line 11327
        .trainerPic = TRAINER_PIC_EDEN,
        .encounterMusic_gender =
#line 11328
F_TRAINER_FEMALE | 
#line 11329
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 11330
        .doubleBattle = FALSE,
#line 11331
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11333
            .nickname = COMPOUND_STRING("Pilfer"),
#line 11333
            .species = SPECIES_NICKIT,
#line 11333
            .gender = TRAINER_MON_MALE,
#line 11337
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11335
            .ability = ABILITY_PRANKSTER,
#line 11334
            .lvl = 5,
            .nature = NATURE_HARDY,
#line 11336
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 11338
                MOVE_TAIL_WHIP,
                MOVE_FAKE_TEARS,
                MOVE_BEAT_UP,
                MOVE_TACKLE,
            },
            },
            {
#line 11343
            .species = SPECIES_TINKATINK,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11345
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11344
            .lvl = 5,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11347
#line 11349
    [DIFFICULTY_NORMAL][TRAINER_DR_EDEN_LAB_2] =
    {
#line 11348
        .trainerName = _("???"),
#line 11350
        .trainerClass = TRAINER_CLASS_BRIGAND,
#line 11351
        .trainerPic = TRAINER_PIC_EDEN,
        .encounterMusic_gender =
#line 11352
F_TRAINER_FEMALE | 
#line 11353
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 11354
        .doubleBattle = FALSE,
#line 11355
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11357
            .nickname = COMPOUND_STRING("Pilfer"),
#line 11357
            .species = SPECIES_NICKIT,
#line 11357
            .gender = TRAINER_MON_MALE,
#line 11361
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11359
            .ability = ABILITY_PRANKSTER,
#line 11358
            .lvl = 5,
            .nature = NATURE_HARDY,
#line 11360
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 11362
                MOVE_TAIL_WHIP,
                MOVE_FAKE_TEARS,
                MOVE_BEAT_UP,
                MOVE_TACKLE,
            },
            },
            {
#line 11367
            .species = SPECIES_FRIGIBAX,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11370
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11368
            .lvl = 5,
            .nature = NATURE_HARDY,
#line 11369
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11372
#line 11374
    [DIFFICULTY_NORMAL][TRAINER_DR_EDEN_LAB_3] =
    {
#line 11373
        .trainerName = _("???"),
#line 11375
        .trainerClass = TRAINER_CLASS_BRIGAND,
#line 11376
        .trainerPic = TRAINER_PIC_EDEN,
        .encounterMusic_gender =
#line 11377
F_TRAINER_FEMALE | 
#line 11378
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 11379
        .doubleBattle = FALSE,
#line 11380
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11382
            .nickname = COMPOUND_STRING("Pilfer"),
#line 11382
            .species = SPECIES_NICKIT,
#line 11382
            .gender = TRAINER_MON_MALE,
#line 11386
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11384
            .ability = ABILITY_PRANKSTER,
#line 11383
            .lvl = 5,
            .nature = NATURE_HARDY,
#line 11385
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            .moves = {
#line 11387
                MOVE_TAIL_WHIP,
                MOVE_FAKE_TEARS,
                MOVE_BEAT_UP,
                MOVE_TACKLE,
            },
            },
            {
#line 11392
            .species = SPECIES_TEDDIURSA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11394
            .iv = TRAINER_PARTY_IVS(0, 0, 0, 0, 0, 0),
#line 11393
            .lvl = 5,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11396
    [DIFFICULTY_NORMAL][TRAINER_DR_R11_FISHER_TAM] =
    {
#line 11397
        .trainerName = _("Tam"),
#line 11398
        .trainerClass = TRAINER_CLASS_FISHER,
#line 11399
        .trainerPic = TRAINER_PIC_DR_FISHER,
        .encounterMusic_gender =
#line 11401
            TRAINER_ENCOUNTER_MUSIC_HIKER,
#line 11402
        .doubleBattle = FALSE,
#line 11403
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11405
            .species = SPECIES_KRABBY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11407
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 11406
            .lvl = 9,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11409
            .species = SPECIES_CORPHISH,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11411
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 11410
            .lvl = 10,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11413
    [DIFFICULTY_NORMAL][TRAINER_DR_HH_ADVENTURER_FINN] =
    {
#line 11414
        .trainerName = _("Finn"),
#line 11415
        .trainerClass = TRAINER_CLASS_ADVENTURER,
#line 11416
        .trainerPic = TRAINER_PIC_DR_ADVENTURER,
        .encounterMusic_gender =
#line 11418
            TRAINER_ENCOUNTER_MUSIC_MALE,
#line 11419
        .doubleBattle = FALSE,
#line 11420
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11422
            .species = SPECIES_VANILLITE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11424
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 11423
            .lvl = 11,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11426
            .nickname = COMPOUND_STRING("Jake"),
#line 11426
            .species = SPECIES_MASCHIFF,
#line 11426
            .gender = TRAINER_MON_MALE,
#line 11429
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 11427
            .lvl = 13,
            .nature = NATURE_HARDY,
#line 11428
            .isShiny = TRUE,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11431
    [DIFFICULTY_NORMAL][TRAINER_DR_HH_REVENANT_ALPHONSE] =
    {
#line 11432
        .trainerName = _("Alphonse"),
#line 11433
        .trainerClass = TRAINER_CLASS_REVENANT,
#line 11434
        .trainerPic = TRAINER_PIC_DR_REVENANT,
        .encounterMusic_gender =
#line 11436
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 11437
        .doubleBattle = FALSE,
#line 11438
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11440
            .species = SPECIES_GASTLY,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11442
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 11441
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11444
            .species = SPECIES_SHEDINJA,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11446
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 11445
            .lvl = 20,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11448
    [DIFFICULTY_NORMAL][TRAINER_DR_HH_WITCH_HELGA] =
    {
#line 11449
        .trainerName = _("Helga"),
#line 11450
        .trainerClass = TRAINER_CLASS_WITCH,
#line 11451
        .trainerPic = TRAINER_PIC_DR_WITCH,
        .encounterMusic_gender =
#line 11452
F_TRAINER_FEMALE | 
#line 11453
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 11454
        .doubleBattle = FALSE,
#line 11455
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 1,
        .party = (const struct TrainerMon[])
        {
            {
#line 11457
            .species = SPECIES_BRAIXEN,
#line 11457
            .gender = TRAINER_MON_FEMALE,
#line 11459
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 11458
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11461
    [DIFFICULTY_NORMAL][TRAINER_DR_HH_ROYAL_OFFICER_DENTH] =
    {
#line 11462
        .trainerName = _("Denth"),
#line 11463
        .trainerClass = TRAINER_CLASS_ROYAL_OFFICER,
#line 11464
        .trainerPic = TRAINER_PIC_DR_ROYAL_OFFICER,
        .encounterMusic_gender =
#line 11466
            TRAINER_ENCOUNTER_MUSIC_INTENSE,
#line 11467
        .doubleBattle = FALSE,
#line 11468
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11470
            .species = SPECIES_HONEDGE,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11472
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 11471
            .lvl = 12,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11474
            .species = SPECIES_NIDORINO,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11476
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 11475
            .lvl = 14,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
#line 11478
    [DIFFICULTY_NORMAL][TRAINER_DR_PELLUCA_BURGLAR] =
    {
#line 11479
        .trainerName = _("Fenwick"),
#line 11480
        .trainerClass = TRAINER_CLASS_BURGLAR,
#line 11481
        .trainerPic = TRAINER_PIC_BURGLAR,
        .encounterMusic_gender =
#line 11483
            TRAINER_ENCOUNTER_MUSIC_SUSPICIOUS,
#line 11484
        .doubleBattle = FALSE,
#line 11485
        .aiFlags = AI_FLAG_BASIC_TRAINER,
        .partySize = 2,
        .party = (const struct TrainerMon[])
        {
            {
#line 11487
            .species = SPECIES_SKWOVET,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11489
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 11488
            .lvl = 7,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
            {
#line 11491
            .species = SPECIES_KLEFKI,
            .gender = TRAINER_MON_RANDOM_GENDER,
#line 11493
            .iv = TRAINER_PARTY_IVS(10, 10, 10, 10, 10, 10),
#line 11492
            .lvl = 8,
            .nature = NATURE_HARDY,
            .dynamaxLevel = MAX_DYNAMAX_LEVEL,
            },
        },
    },
