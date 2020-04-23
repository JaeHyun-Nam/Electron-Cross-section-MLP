#Data 8:1:1, augmentation
a=1092
b=548
sigma=0.000948
alph=0.00323
lr=1.497e-5
num_class=4
optimizer=optimizers.adam(lr=lr,decay=0)
train_data_n,test_data_n,train_label_n,test_label_n=train_test_split(train_data,train_Label,test_size=0.2,random_state=None)
test_data_n,val_data_n,test_label_n,val_label_n=train_test_split(test_data_n,test_label_n,test_size=0.5,random_state=None)
(train_data_aug,train_label_aug)=augment(train_data_n,train_label_n,74,26,2,19,num_pair,sigma)# balance imbalanced data
(test_data_aug,test_label_aug)=(test_data_n,test_label_n)
(val_data_aug,val_label_aug)=augment(val_data_n,val_label_n,37,13,1,8,num_pair,0)# No augmentation, just over sampling of lakced data
train_label_aug=np_utils.to_categorical(train_label_aug)
val_label_aug=np_utils.to_categorical(val_label_aug)
test_label_aug=np_utils.to_categorical(test_label_aug)
def classifier():
    model = Sequential()
    model.add(Dense(int(a), input_dim=num_pair, init='normal'))
    model.add(LeakyReLU(alpha = alph))
    model.add(Dense(int(b), init='normal'))
    model.add(LeakyReLU(alpha = alph))
    model.add(Dense(num_class, init='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])
    return model
    model=classifier()
es=EarlyStopping(monitor='val_loss',mode='min',verbose=0,patience=25)
mc=ModelCheckpoint('',monitor='val_loss',mode='min',save_best_only=True)
model.fit(train_data_aug,train_label_aug,validation_data=(val_data_aug,val_label_aug),nb_epoch=300,batch_size=batch_size,verbose=0,validation_freq=1,callbacks=[es,mc])