import { Module } from '@nestjs/common';
import { InventarioService } from './inventario.service';
import { InventarioController } from './inventario.controller';
import { InventarioSchema } from './Schema/inventario';
import { MongooseModule } from '@nestjs/mongoose';

@Module({
  imports: [MongooseModule.forFeature([{ name: 'Inventario', schema: InventarioSchema }])],
  providers: [InventarioService],
  controllers: [InventarioController]
})
export class InventarioModule {}
