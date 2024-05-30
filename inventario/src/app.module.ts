import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { MongooseModule } from '@nestjs/mongoose';
import { InventarioModule } from './inventario/inventario.module';

@Module({
  imports: [
    MongooseModule.forRoot('mongodb+srv://kevinfajardo1:13demayo@cluster-udla.vajun2h.mongodb.net/inventario?retryWrites=true&w=majority&appName=Cluster-Udla'),
    InventarioModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
